import os
import click
import json
from ..utils.config import PROJECT_ROOT
from .utils.uninstalldjangoapp import uninstall_django_app

@click.command()
@click.option('--site', type=str, help="The name of the site where the app will be uninstalled.")
@click.option('--app', type=str, help="The name of the app to uninstall.")
def uninstallapp(site, app):
    """Uninstall an app from a selected site and update sites.json."""

    # Load sites from sites.json
    sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
    if os.path.exists(sites_json_path):
        with open(sites_json_path, "r") as json_file:
            sites = json.load(json_file)
    else:
        click.echo("No sites found in sites.json.")
        return

    # Prompt for site if not provided
    if not site:
        click.echo("Select a site to uninstall the app:")
        for i, site_entry in enumerate(sites, 1):
            click.echo(f"{i}. {site_entry['site_name']}")

        site_choice = click.prompt("Enter the number of the site", type=int)

        if site_choice < 1 or site_choice > len(sites):
            click.echo("Invalid site selection.")
            return

        selected_site = sites[site_choice - 1]
    else:
        selected_site = next((s for s in sites if s['site_name'] == site), None)
        if not selected_site:
            click.echo(f"Site '{site}' not found in sites.json.")
            return

    # Ensure the site has installed apps
    if "installed_apps" not in selected_site or not selected_site["installed_apps"]:
        click.echo(f"No apps installed in '{selected_site['site_name']}'.")
        return

    # Prompt for app if not provided
    if not app:
        click.echo(f"Select an app to uninstall from '{selected_site['site_name']}':")
        for i, app_entry in enumerate(selected_site["installed_apps"], 1):
            click.echo(f"{i}. {app_entry}")

        app_choice = click.prompt("Enter the number of the app you want to uninstall", type=int)

        if app_choice < 1 or app_choice > len(selected_site["installed_apps"]):
            click.echo("Invalid app selection.")
            return

        selected_app = selected_site["installed_apps"][app_choice - 1]
    else:
        selected_app = app
        if selected_app not in selected_site["installed_apps"]:
            click.echo(f"App '{selected_app}' is not installed in '{selected_site['site_name']}'.")
            return

    # Simulate uninstalling the app (e.g., removing files, undoing migrations, etc.)
    click.echo(f"Uninstalling '{selected_app}' from '{selected_site['site_name']}'...")

    # Remove the app from the installed_apps list
    selected_site["installed_apps"].remove(selected_app)

    with open(sites_json_path, "w") as json_file:
        json.dump(sites, json_file, indent=4)

    # Call the uninstall utility
    uninstall_django_app(selected_site['site_name'], selected_app, PROJECT_ROOT)

    click.echo(f"The app '{selected_app}' has been successfully uninstalled from '{selected_site['site_name']}'.")


if __name__ == '__main__':
    uninstallapp()
