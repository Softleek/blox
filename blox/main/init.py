import json
import os
import subprocess
import click

from ..utils.file_operations import ensure_file_exists

@click.command()
@click.argument("name", required=False, default=".")
def init(name):
    """Initialize a new project similar to bench init."""
    
    # Determine project root
    project_root = os.path.abspath(name)
    if name != ".":
        os.makedirs(project_root, exist_ok=True)
    
    # Define necessary directories
    directories = ["apps", "config", "logs", "sites",]
    for directory in directories:
        os.makedirs(os.path.join(project_root, directory), exist_ok=True)
    
    # Create necessary files
    sites_json_path = os.path.join(project_root, "config", "sites.json")
    procfile_path = os.path.join(project_root, "Procfile") 
    procfile_path = os.path.join(project_root, "blox.config") 
    
    ensure_file_exists(sites_json_path, initial_data=[])
    
    with open(procfile_path, "w") as procfile:
        procfile.write("""
web: blox start
redis_cache: redis-server config/redis_cache.conf
redis_queue: redis-server config/redis_queue.conf
worker: blox worker
schedule: blox schedule
""")
    
    # Clone mainsite into sites/default
    site_path = os.path.join(project_root, "sites", )
    repo_url = "https://github.com/Softleek/mainsite.git"
    
    try:
        subprocess.check_call(["git", "clone", repo_url, site_path])
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to clone the repository: {e}")
        return
    
    # Load sites.json
    try:
        with open(sites_json_path, "r") as json_file:
            sites = json.load(json_file) or []
    except json.JSONDecodeError:
        sites = []
    
    # Assign available ports
    django_ports = [site.get("django_port") for site in sites]
    next_django_port = 8000
    while next_django_port in django_ports:
        next_django_port += 1
    
    nextjs_ports = [site.get("nextjs_port") for site in sites]
    next_nextjs_port = 3000
    while next_nextjs_port in nextjs_ports:
        next_nextjs_port += 1
    
    # Update sites.json
    site_info = {
        "name": "default",
        "django_port": next_django_port,
        "nextjs_port": next_nextjs_port,
        "developer_mode": True,
    }
    
    sites.append(site_info)
    with open(sites_json_path, "w") as json_file:
        json.dump(sites, json_file, indent=4)
    
    click.echo("Project initialized successfully!")
    
    # Run post-install commands
    try:
        subprocess.check_call(["blox", "install"])
        subprocess.check_call(["blox", "migrate"])
        subprocess.check_call(["blox", "django", "createsuperuser"])
        click.echo("Successfully initialized project.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to run post-creation commands: {e}", err=True)
