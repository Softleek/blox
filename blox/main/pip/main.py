import os
import subprocess
import click
import sys
from ...utils.config import PROJECT_ROOT, APPS_PATH
import json

def install_libraries(libraries, app_name=None, sites=None):
    venv_path = os.path.join(PROJECT_ROOT, 'env')
    if not os.path.exists(venv_path):
        click.echo("Virtual environment not found. Please run 'blox setup' first.")
        return

    python_executable = os.path.join(venv_path, 'bin', 'python')
    if sys.platform.startswith('win'):
        python_executable = os.path.join(venv_path, 'Scripts', 'python.exe')

    if app_name:
        requirements_file = os.path.join(APPS_PATH, f'{app_name}/requirements.txt')

        # Add libraries to requirements file
        with open(requirements_file, 'a') as f:
            for library in libraries:
                f.write(f"{library}\n")
        click.echo(f"Added libraries to {requirements_file}")

    # Install libraries on the specified sites
    for site in sites:
        django_path = os.path.join(PROJECT_ROOT, 'sites', site, 'django')
        if os.path.exists(django_path):
            try:
                for library in libraries:
                    subprocess.check_call(
                        [python_executable, '-m', 'pip', 'install', library]
                    )
                click.echo(f"Installed libraries for site '{site}' successfully.")
            except subprocess.CalledProcessError as e:
                click.echo(f"Error installing libraries for site '{site}': {e}")

@click.group()
def pip():
    """
    Manage Python packages for the project.
    """
    pass

@click.command()
@click.argument('libraries', nargs=-1)
@click.option('--app', type=str, help='Specify a custom app to update its requirements.txt')
@click.option('--site', type=str, help='Specify a site to install the libraries. If not provided, a selection prompt will appear.')
def install(libraries, app, site):
    """
    Install the specified Python libraries in the project.
    Usage: blox pip install <library_name> [<library_name>...] [--app <app_name>] [--site <site_name>]
    """
    # Load sites from sites.json
    sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
    if os.path.exists(sites_json_path):
        with open(sites_json_path, "r") as json_file:
            sites = json.load(json_file)
    else:
        click.echo("No sites found in sites.json.")
        return

    if not site:
        click.echo("Select sites to install libraries:")
        for i, site_entry in enumerate(sites, 1):
            click.echo(f"{i}. {site_entry['site_name']}")

        site_choices = click.prompt("Enter the numbers of the sites separated by commas", type=str)
        selected_sites = [sites[int(num) - 1]['site_name'] for num in site_choices.split(',') if num.isdigit()]
    else:
        selected_sites = [site]

    # Check for apps in selected sites
    app_names = set()
    for selected_site in selected_sites:
        site_info = next((s for s in sites if s['site_name'] == selected_site), None)
        if site_info and 'installed_apps' in site_info:
            app_names.update(site_info['installed_apps'])

    if app and app not in app_names:
        click.echo(f"App '{app}' not found in the selected sites.")
        return

    if not app:
        click.echo("Select an app to install the libraries:")
        for i, app_entry in enumerate(app_names, 1):
            click.echo(f"{i}. {app_entry}")

        app_choice = click.prompt("Enter the number of the app", type=int)
        if app_choice < 1 or app_choice > len(app_names):
            click.echo("Invalid app selection.")
            return
        
        app = list(app_names)[app_choice - 1]

    try:
        install_libraries(libraries, app, selected_sites)
        click.echo("Libraries installed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error installing libraries: {e}")

@click.command()
@click.argument('libraries', nargs=-1)
@click.option('--app', type=str, help='Specify a custom app to update its requirements.txt')
@click.option('--site', type=str, help='Specify a site to install the libraries. If not provided, a selection prompt will appear.')
def i(libraries, app, site):
    """
    Install the specified Python libraries in the project using the alias 'i'.
    Usage: blox pip i <library_name> [<library_name>...] [--app <app_name>] [--site <site_name>]
    """
    install(libraries, app, site)

pip.add_command(install)
pip.add_command(i)
