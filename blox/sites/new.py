import json
import os
import subprocess

import click

from ..utils.config import PROJECT_ROOT
from ..sites.migrate.migrate import run_migration
from ..utils.file_operations import ensure_file_exists

@click.command()
@click.argument("site_name")
def newsite(site_name):
    """Clone the mainsite repository and add it to sites.json with available ports."""

    # Define the repository URL and target path
    repo_url = "https://github.com/Softleek/mainsite.git"
    target_path = os.path.join(PROJECT_ROOT, "sites")

    # Clone the repository directly into the site name
    try:
        subprocess.check_call(
            ["git", "clone", repo_url, os.path.join(target_path, site_name)]
        )
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to clone the repository: {e}")
        return

    # Load existing sites.json or initialize an empty list
    sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
    sites = []

    # Check if sites.json exists and load it if it has valid content
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

    # Determine the next available Django and Next.js ports
    django_ports = [site.get("django_port") for site in sites]
    next_django_port = 8000
    while next_django_port in django_ports:
        next_django_port += 1

    next_nextjs_port = 3000
    nextjs_ports = [site.get("nextjs_port") for site in sites]
    while next_nextjs_port in nextjs_ports:
        next_nextjs_port += 1

    # Prepare the site information
    site_info = {
        "site_name": site_name,
        "django_port": next_django_port,
        "nextjs_port": next_nextjs_port,
        "developer_mode": True,
    }

    # Add the new site information to the list
    sites.append(site_info)

    # Write the updated list back to sites.json
    with open(sites_json_path, "w") as json_file:
        json.dump(sites, json_file, indent=4)

    click.echo(
        f"The site '{site_name}' has been created and added to sites.json with Django port {next_django_port} and Next.js port {next_nextjs_port}."
    )

    # After the site creation, run the additional commands
    try:
        # Flag before running 'blox install'
        click.echo(
            click.style(f"Running 'blox install' for site '{site_name}'...", fg="cyan")
        )

        # Run 'blox install' command
        subprocess.check_call(["blox", "install", "--site", site_name])

        # Flag after running 'blox install'
        click.echo(
            click.style(
                f"Successfully ran 'blox install' for site '{site_name}'.", fg="green"
            )
        )

        # Flag before running 'blox migrate'
        click.echo(
            click.style(f"Running 'blox migrate' for site '{site_name}'...", fg="cyan")
        )

        # Run 'blox migrate' command
        subprocess.check_call(["blox", "migrate", "--site", site_name])

        # Flag after running 'blox migrate'
        click.echo(
            click.style(
                f"Successfully ran 'blox migrate' for site '{site_name}'.", fg="green"
            )
        )

        # Flag before running 'blox django createsuperuser'
        click.echo(
            click.style(
                f"Running 'blox django createsuperuser' for site '{site_name}'...",
                fg="cyan",
            )
        )

        # Run 'blox django createsuperuser' command
        subprocess.check_call(
            ["blox", "django", "createsuperuser", "--site", site_name]
        )

        # Flag after running 'blox django createsuperuser'
        click.echo(
            click.style(
                f"Successfully ran 'blox django createsuperuser' for site '{site_name}'.",
                fg="green",
            )
        )

    except subprocess.CalledProcessError as e:
        click.echo(
            click.style(
                f"Failed to run one of the post-creation commands: {e}", fg="red"
            )
        )
    run_migration()
