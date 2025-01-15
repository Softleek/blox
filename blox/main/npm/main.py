import json
import os
import subprocess

import click

from ...utils.config import APPS_PATH, PROJECT_ROOT


def update_package_json(app_name, libraries):
    package_json_path = os.path.join(APPS_PATH, app_name, "package.json")

    if not os.path.exists(package_json_path):
        click.echo(f"No package.json found for app '{app_name}'.")
        return

    with open(package_json_path, "r") as f:
        package_json = json.load(f)

    if "dependencies" not in package_json:
        package_json["dependencies"] = {}

    for library in libraries:
        package_json["dependencies"][library] = "*"  # Use "*" or specify a version

    with open(package_json_path, "w") as f:
        json.dump(package_json, f, indent=4)

    click.echo(f"Updated {package_json_path} with new dependencies.")


def install_npm_packages(libraries, app_name, site):
    nextjs_path = os.path.join(PROJECT_ROOT, "sites", site, "nextjs")

    if not os.path.exists(nextjs_path):
        click.echo(f"Next.js path for site '{site}' not found.")
        return

    # Determine the command for the current operating system
    npm_command = ["npm", "install"] + list(libraries)

    # Execute the npm command in the Next.js directory
    try:
        if os.name == "nt":  # Windows
            subprocess.check_call(npm_command, cwd=nextjs_path, shell=True)
        else:  # Unix-based systems
            subprocess.check_call(npm_command, cwd=nextjs_path)
        click.echo("Libraries installed successfully in core Next.js project.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error installing libraries in core Next.js project: {e}")


@click.group()
def npm():
    """
    Manage NPM packages for the project.
    """


@click.command()
@click.argument("libraries", nargs=-1)
@click.option("--app", type=str, help="Specify a custom app to update its package.json")
@click.option(
    "--site",
    type=str,
    help="Specify a site to install the libraries. If not provided, a selection prompt will appear.",
)
def install(libraries, app, site):
    """
    Install the specified NPM packages in the project.
    Usage: blox npm install <library_name> [<library_name>...] [--app <app_name>] [--site <site_name>]
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

        site_choices = click.prompt(
            "Enter the numbers of the sites separated by commas", type=str
        )
        selected_sites = [
            sites[int(num) - 1]["site_name"]
            for num in site_choices.split(",")
            if num.isdigit()
        ]
    else:
        selected_sites = [site]

    # Check for apps in selected sites
    app_names = set()
    for selected_site in selected_sites:
        site_info = next((s for s in sites if s["site_name"] == selected_site), None)
        if site_info and "installed_apps" in site_info:
            app_names.update(site_info["installed_apps"])

    if app and app not in app_names:
        click.echo(f"App '{app}' not found in the selected sites.")
        return

    if not app:
        click.echo("Select an app to install the libraries:")
        for i, app_entry in enumerate(app_names, 1):
            click.echo(f"{i}. {app_entry}")

        app_choice = click.prompt("Enter the number of the app", type=int)
        if not app_choice:
            install_npm_packages(libraries, None, selected_site)
            return  # Exit early after installing for all selected sites

        if app_choice < 1 or app_choice > len(app_names):

            click.echo("Invalid app selection.")
            return

        app = list(app_names)[app_choice - 1]

    if app:
        update_package_json(app, libraries)

    for selected_site in selected_sites:
        install_npm_packages(libraries, app, selected_site)


@click.command()
@click.argument("libraries", nargs=-1)
@click.option("--app", type=str, help="Specify a custom app to update its package.json")
@click.option(
    "--site",
    type=str,
    help="Specify a site to install the libraries. If not provided, a selection prompt will appear.",
)
def i(libraries, app, site):
    """
    Install the specified NPM packages in the project using the alias 'i'.
    Usage: blox npm i <library_name> [<library_name>...] [--app <app_name>] [--site <site_name>]
    """
    install(libraries, app, site)


npm.add_command(install)
npm.add_command(i)
