import json
import os
import subprocess
import sys

import click

from ...utils.config import PROJECT_ROOT
from ...utils.file_operations import ensure_file_exists

def get_python_executable():
    """Get the path to the Python executable in the virtual environment."""
    venv_path = os.path.join(PROJECT_ROOT, "env")
    if not os.path.exists(venv_path):
        click.echo("Virtual environment not found. Please run 'blox setup' first.")
        raise FileNotFoundError("Virtual environment not found.")

    python_executable = os.path.join(venv_path, "bin", "python")
    if sys.platform.startswith("win"):
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")

    return python_executable


@click.command()
@click.argument("command")
@click.argument("args", nargs=-1)
@click.option("--site", default=None, help="Specify a site.")
def django(command, args, site=None):
    """Run Django management commands."""
    if command not in [
        "migrate",
        "makemigrations",
        "createsuperuser",
        "runserver",
        "shell",
        "createuser",
    ]:
        click.echo(
            "Invalid command. Available commands: migrate, makemigrations, createsuperuser, runserver, shell, createuser."
        )
        return

    # Load sites from sites.json
    sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
    ensure_file_exists(sites_json_path, initial_data=[])
    if os.path.exists(sites_json_path):
        with open(sites_json_path, "r") as json_file:
            sites = json.load(json_file)
    else:
        click.echo("No sites found in sites.json.")
        return

    # Prompt for site if not provided
    if not site:
        click.echo("Select a site to migrate:")
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

    django_path = os.path.join(
        PROJECT_ROOT, "sites", selected_site["site_name"], "django"
    )

    venv_path = os.path.join(PROJECT_ROOT, "env")
    if not os.path.exists(venv_path):
        click.echo("Virtual environment not found. Please run 'blox setup' first.")
        return

    python_executable = os.path.join(venv_path, "bin", "python")
    if sys.platform.startswith("win"):
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")

    # Construct the command to be executed
    command_list = [python_executable, "manage.py", command] + list(args)

    # Execute the command
    subprocess.run(command_list, cwd=django_path)
    click.echo(f"Executed '{command}' command for site '{site}'.")


if __name__ == "__main__":
    django()
