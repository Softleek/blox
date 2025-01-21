import json
import os
import subprocess
import random
import string
import click
import platform

from ..utils.config import PROJECT_ROOT
from ..utils.file_operations import ensure_file_exists

def generate_random_password(length=12):
    """Generate a random password with letters and digits only (avoids special character issues)."""
    characters = string.ascii_letters + string.digits  # No special characters
    return ''.join(random.choice(characters) for _ in range(length))

@click.command()
@click.argument("site_name")
def newsite(site_name):
    """Clone the mainsite repository, create a database, and add it to sites.json."""

    # Load existing sites.json or initialize an empty list
    sites_json_path = os.path.join(PROJECT_ROOT, "sites", "sites.json")
    sites = []

    ensure_file_exists(sites_json_path, initial_data=[])
    try:
        with open(sites_json_path, "r") as json_file:
            content = json_file.read().strip()
            if content:
                sites = json.loads(content)
    except json.JSONDecodeError:
        click.echo(
            f"Invalid JSON in {sites_json_path}. Initializing an empty list."
        )
    
    # Prompt for root password
    root_password = click.prompt("Enter database root password", hide_input=True)
    
    # Create the database using Windows CMD
    db_name = f"{site_name}_db"
    
    try:
        # Create database
        subprocess.run(
            ["mysql", "-u", "root", "-p" + root_password, "-e", f"CREATE DATABASE {db_name};"],
            check=True,
        )
        click.echo(click.style(f"Database '{db_name}' created successfully.", fg="green"))
    except subprocess.CalledProcessError as e:
        click.echo(click.style(f"Database creation failed: {e}", fg="red"))
        return
    
    # Create a new MySQL user and grant them admin privileges
    db_user = site_name
    db_user_password = generate_random_password()
    try:
        # Create user and grant privileges
        subprocess.run(
            [
                "mysql", "-u", "root", "-p" + root_password,
                "-e", f"CREATE USER '{db_user}'@'localhost' IDENTIFIED BY '{db_user_password}';"
            ],
            check=True,
        )
        subprocess.run(
            [
                "mysql", "-u", "root", "-p" + root_password,
                "-e", f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'localhost';"
            ],
            check=True,
        )
        subprocess.run(
            [
                "mysql", "-u", "root", "-p" + root_password,
                "-e", f"FLUSH PRIVILEGES;"
            ],
            check=True,
        )
        click.echo(click.style(f"User '{db_user}' created and granted admin privileges.", fg="green"))
    except subprocess.CalledProcessError as e:
        click.echo(click.style(f"Failed to create user or grant privileges: {e}", fg="red"))
        return
    
    # Prepare the site information
    site_info = {
        "site_name": site_name,
        "database": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": db_name,
            "USER": db_user,
            "PASSWORD": db_user_password,
            "HOST": "localhost",
        },
        "installed_apps": [],
    }
    
    # Add the new site information to the list
    sites.append(site_info)
    
    # Save the updated sites.json
    with open(sites_json_path, "w") as json_file:
        json.dump(sites, json_file, indent=4)
    
    click.echo(click.style(f"Site '{site_name}' added to sites.json.", fg="green"))

    # Run post-creation commands
    try:
        click.echo(click.style(f"Running migrations for site '{site_name}'...", fg="cyan"))
        subprocess.check_call(["blox", "migrate", "--site", site_name])
        click.echo(click.style(f"Successfully migrated '{site_name}'.", fg="green"))

        click.echo(click.style(f"Creating superuser...", fg="cyan"))
        subprocess.check_call(["blox", "django", "createsuperuser_tenant", site_name])
        click.echo(click.style(f"Successfully created site - '{site_name}'.", fg="green"))
    
    except subprocess.CalledProcessError as e:
        click.echo(click.style(f"Failed to run post-creation commands: {e}", fg="red"))
