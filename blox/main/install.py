import os
import subprocess
import click
import json
from ..utils.config import PROJECT_ROOT, APPS_PATH

def activate_virtualenv():
    venv_path = os.path.join(PROJECT_ROOT, 'env')
    if not os.path.exists(venv_path):
        click.echo("Virtual environment not found. Please run 'blox setup' first.")
        return False
    
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
    else:  # Unix-based
        activate_script = os.path.join(venv_path, 'bin', 'activate')

    return activate_script

def app_install_python_packages(app):
    requirements_file = os.path.join(APPS_PATH, app, 'requirements.txt')
    if os.path.exists(requirements_file):
        click.echo(f"Installing packages from {requirements_file}...")
        subprocess.check_call(['pip', 'install', '-r', requirements_file])
        
def install_python_packages(site):
    site_requirements = os.path.join(PROJECT_ROOT, 'sites', site, 'django', 'requirements.txt')
    if os.path.exists(site_requirements):
        click.echo(f"Installing packages from {site_requirements}...")
        subprocess.check_call(['pip', 'install', '-r', site_requirements])
        
def app_install_npm_packages(site, app):
    package_json_path = os.path.join(APPS_PATH, app, 'package.json')
    if os.path.exists(package_json_path):
        click.echo(f"Installing packages from {package_json_path}...")
        
        nextjs_path = os.path.join(PROJECT_ROOT, 'sites', site, 'nextjs')
        
        # Read package.json to get dependencies and devDependencies
        with open(package_json_path, 'r') as f:
            package_data = json.load(f)
        
        dependencies = package_data.get('dependencies', {})
        dev_dependencies = package_data.get('devDependencies', {})
        
        # Combine all dependencies
        all_dependencies = {**dependencies, **dev_dependencies}
        

        # Determine the command for the current operating system
        npm_command = ['npm', 'install'] + list(all_dependencies.keys())
        
        # Execute the npm command in the Next.js directory
        try:
            if os.name == 'nt':  # Windows
                subprocess.check_call(npm_command, cwd=nextjs_path, shell=True)
            else:  # Unix-based systems
                subprocess.check_call(npm_command, cwd=nextjs_path)
            click.echo("Libraries installed successfully in core Next.js project.")
        except subprocess.CalledProcessError as e:
            click.echo(f"Error installing libraries in core Next.js project: {e}")
    else:
        click.echo(f"package.json not found for app '{app}'.")     
           
def install_npm_packages(site):
        nextjs_path = os.path.join(PROJECT_ROOT, 'sites', site, 'nextjs')
  
        # Determine the command for the current operating system
        npm_command = ['npm', 'install']
        
        # Execute the npm command in the Next.js directory
        try:
            if os.name == 'nt':  # Windows
                subprocess.check_call(npm_command, cwd=nextjs_path, shell=True)
            else:  # Unix-based systems
                subprocess.check_call(npm_command, cwd=nextjs_path)
            click.echo("Libraries installed successfully in core Next.js project.")
        except subprocess.CalledProcessError as e:
            click.echo(f"Error installing libraries in core Next.js project: {e}")


def install_dependencies(site):
    sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
    with open(sites_json_path, "r") as json_file:
        sites = json.load(json_file)
    
    site_info = next((s for s in sites if s['site_name'] == site), None)
    if not site_info:
        click.echo(f"Site '{site}' not found.")
        return

    installed_apps = site_info.get('installed_apps', [])
    for app in installed_apps:
        app_install_python_packages(app)
        app_install_npm_packages(site, app)
    install_python_packages(site)
    install_npm_packages(site)

@click.command()
@click.option('--site', type=str, help='Specify a site to install dependencies. If not provided, a selection prompt will appear.')
def install(site):
    """
    Install all dependencies for the specified site.
    Usage: blox install --site <site_name>
    """
    # Activate the virtual environment
    activate_script = activate_virtualenv()
    if activate_script:
        if os.name == 'nt':
            os.system(activate_script)
        else:
            subprocess.call(['source', activate_script], shell=True)

    if not site:
        # Load sites from sites.json
        sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
        with open(sites_json_path, "r") as json_file:
            sites = json.load(json_file)

        click.echo("Select a site to install dependencies:")
        for i, site_entry in enumerate(sites, 1):
            click.echo(f"{i}. {site_entry['site_name']}")

        site_choices = click.prompt("Enter the number of the site", type=str)
        selected_site = sites[int(site_choices) - 1]['site_name']
    else:
        selected_site = site

    install_dependencies(selected_site)
    click.echo(f"Dependencies installed successfully for site '{selected_site}'.")

@click.command()
@click.option('--site', type=str, help='Specify a site to install dependencies. If not provided, a selection prompt will appear.')
def i(site):
    """
    Install all dependencies for the specified site.
    Usage: blox i --site <site_name>
    """
    # Activate the virtual environment
    activate_script = activate_virtualenv()
    if activate_script:
        if os.name == 'nt':
            os.system(activate_script)
        else:
            subprocess.call(['source', activate_script], shell=True)

    if not site:
        # Load sites from sites.json
        sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
        with open(sites_json_path, "r") as json_file:
            sites = json.load(json_file)

        click.echo("Select a site to install dependencies:")
        for i, site_entry in enumerate(sites, 1):
            click.echo(f"{i}. {site_entry['site_name']}")

        site_choices = click.prompt("Enter the number of the site", type=str)
        selected_site = sites[int(site_choices) - 1]['site_name']
    else:
        selected_site = site

    install_dependencies(selected_site)
    click.echo(f"Dependencies installed successfully for site '{selected_site}'.")


