import json
import os
import shutil
import subprocess

import click

from ..utils.config import PROJECT_ROOT
from ..sites.migrate.migrate import run_migration


@click.command()
@click.option("--app", type=str, help="The name of the app to delete.")
def dropapp(app):
    """Delete the specified Django app, uninstall it from all sites using `blox uninstallapp`, and remove it from the configuration."""

    # Path to the custom app directory
    apps_txt_path = os.path.join(PROJECT_ROOT, "config", "apps.txt")
    if not os.path.exists(apps_txt_path):
        click.echo("No apps found in apps.txt.")
        return

    # Load apps from apps.txt
    with open(apps_txt_path, "r") as settings_file:
        apps = [
            line.strip()
            for line in settings_file.readlines()
            if line.strip() and not line.startswith("#")
        ]

    # Prompt for app if not provided
    if not app:
        click.echo("Select an app to delete:")
        for i, app_entry in enumerate(apps, 1):
            click.echo(f"{i}. {app_entry}")

        app_choice = click.prompt("Enter the number of the app to delete", type=int)

        if app_choice < 1 or app_choice > len(apps):
            click.echo("Invalid app selection.")
            return

        selected_app = apps[app_choice - 1]
    else:
        selected_app = app
        if selected_app not in apps:
            click.echo(f"App '{app}' not found in apps.txt.")
            return

    # Confirm the deletion
    confirm = click.confirm(
        f"Are you sure you want to delete the app '{selected_app}'?", default=False
    )
    if not confirm:
        click.echo("App deletion canceled.")
        return

    # Uninstall the app from all sites using `blox uninstallapp`
    sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
    if not os.path.exists(sites_json_path):
        click.echo("No sites.json configuration found.")
        return

    # Load all sites from sites.json
    with open(sites_json_path, "r") as sites_file:
        sites = json.load(sites_file)

    for site in sites:
        site_name = site.get("site_name")
        try:
            click.echo(
                f"Running `blox uninstallapp` for app '{selected_app}' on site '{site_name}'..."
            )
            # Run the `blox uninstallapp` command
            subprocess.check_call(
                ["blox", "uninstallapp", "--site", site_name, "--app", selected_app],
                cwd=PROJECT_ROOT,
            )
            click.echo(
                f"Successfully uninstalled app '{selected_app}' from site '{site_name}'."
            )
        except subprocess.CalledProcessError as e:
            click.echo(
                f"Failed to uninstall app '{selected_app}' from site '{site_name}': {e}"
            )

    # Path to the app folder
    custom_app_path = os.path.join(PROJECT_ROOT, "apps", selected_app)

    # Delete the app folder using PowerShell with admin privileges on Windows
    try:
        if os.path.exists(custom_app_path):
            click.echo(
                f"Attempting to delete the app folder '{custom_app_path}' with admin privileges..."
            )

            if os.name == "nt":  # Check if Windows
                powershell_command = f'Remove-Item -Recurse -Force "{custom_app_path}"'
                subprocess.check_call(
                    ["powershell", "-Command", powershell_command], shell=True
                )
            else:
                # For Unix-based systems, use shutil.rmtree
                shutil.rmtree(custom_app_path)

            click.echo(f"Deleted the app folder '{custom_app_path}'.")
        else:
            click.echo(f"App folder '{custom_app_path}' does not exist.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error deleting app folder: {e}")
        return

    # Remove the app entry from apps.txt
    with open(apps_txt_path, "w") as settings_file:
        for line in apps:
            if line.strip() != selected_app:
                settings_file.write(line + "\n")

    click.echo(f"The app '{selected_app}' has been removed from apps.txt.")
    
    run_migration()