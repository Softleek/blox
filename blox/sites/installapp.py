import os
import click
import json
from ..utils.config import PROJECT_ROOT, DJANGO_PATH, DEFAULT_SITE
from .utils.installdjangoapp import install_django_app

@click.command()
@click.option('--site', type=str, help="The name of the site where the app will be installed.")
@click.option('--app', type=str, help="The name of the app to install.")
def installapp(site, app):
    """Install an app into a selected site and update sites.json."""

    # Load sites from sites.json
    sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
    if os.path.exists(sites_json_path):
        with open(sites_json_path, "r") as json_file:
            sites = json.load(json_file)
    else:
        click.echo("No sites found in sites.json.")
        return

    # Select or prompt for the site
    if not site:
        click.echo("Select a site to install the app into:")
        for i, site_entry in enumerate(sites, 1):
            click.echo(f"{i}. {site_entry['site_name']}")

        site_choice = click.prompt("Enter the number of the site", type=int)

        if site_choice < 1 or site_choice > len(sites):
            click.echo("Invalid site selection.")
            return

        selected_site = sites[site_choice - 1]
    else:
        selected_site = next((s for s in sites if s["site_name"] == site), None)
        if not selected_site:
            click.echo(f"Site '{site}' not found in sites.json.")
            return

    # Set django_path based on the selected site
    django_path = os.path.join(PROJECT_ROOT, "sites", selected_site["site_name"], "django")

    # Load apps from apps.txt
    apps_txt_path = os.path.join(PROJECT_ROOT, "config", "apps.txt")
    if os.path.exists(apps_txt_path):
        with open(apps_txt_path, "r") as apps_file:
            apps = [line.strip() for line in apps_file if line.strip() and not line.startswith("#")]
    else:
        click.echo("No apps.txt file found.")
        return

    if not apps:
        click.echo("No available apps found in apps.txt.")
        return

    # Prompt for app if not provided
    if not app:
        click.echo(f"Select an app to install into '{selected_site['site_name']}':")
        for i, app_entry in enumerate(apps, 1):
            click.echo(f"{i}. {app_entry}")

        app_choice = click.prompt("Enter the number of the app you want to install", type=int)

        if app_choice < 1 or app_choice > len(apps):
            click.echo("Invalid app selection.")
            return

        selected_app = apps[app_choice - 1]
    else:
        selected_app = app
        if selected_app not in apps:
            click.echo(f"App '{selected_app}' not found in apps.txt.")
            return

    # Check if the app is already installed in the site
    if "installed_apps" not in selected_site:
        selected_site["installed_apps"] = []

    if selected_app in selected_site["installed_apps"]:
        click.echo(f"The app '{selected_app}' is already installed in '{selected_site['site_name']}'.")
        return

    # Install the app using the external function
    click.echo(f"Installing '{selected_app}' into '{selected_site['site_name']}'...")
    install_django_app(selected_site["site_name"], selected_app, PROJECT_ROOT)

    # Update the selected site's installed_apps
    selected_site["installed_apps"].append(selected_app)

    # Replace the updated site in the sites list
    for i, site_entry in enumerate(sites):
        if site_entry["site_name"] == selected_site["site_name"]:
            sites[i] = selected_site
            break

    # Write the updated sites.json
    with open(sites_json_path, "w") as json_file:
        json.dump(sites, json_file, indent=4)

    click.echo(f"The app '{selected_app}' has been successfully installed in '{selected_site['site_name']}'.")
