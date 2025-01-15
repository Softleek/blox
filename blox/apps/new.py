import os
import shutil
import subprocess

import click

from ..utils.config import PROJECT_ROOT
from .utils.file_creater import create_files_from_templates
from ..sites.migrate.migrate import run_migration


@click.command()
@click.argument("app_name")
@click.option(
    "--title",
    prompt="App Title",
    default="My Blox App",
    help="The title of your app",
    show_default=True,
)
@click.option(
    "--description",
    prompt="App Description",
    default="This is a new Blox app.",
    help="A short description of your app",
    show_default=True,
)
@click.option(
    "--publisher",
    prompt="App Publisher",
    default="Blox Technologies",
    help="The publisher of your app",
    show_default=True,
)
@click.option(
    "--email",
    prompt="Publisher Email",
    default="contact@example.io",
    help="The email of the publisher",
    show_default=True,
)
@click.option(
    "--license",
    prompt="App License",
    type=click.Choice(["MIT", "GPL-3.0", "Apache-2.0"], case_sensitive=False),
    default="MIT",
    help="License for the app",
    show_default=True,
)
def newapp(app_name, title, description, publisher, email, license):
    """Create a new Blox-style app with the specified name."""

    # Define paths
    temp_app_path = os.path.join(PROJECT_ROOT, "apps", f"temp_{app_name}")
    final_app_path = os.path.join(PROJECT_ROOT, "apps", app_name)

    # Check if the app already exists
    if os.path.exists(final_app_path):
        click.echo(f"The app '{app_name}' already exists.")
        return

    # Create the temporary app directory
    os.makedirs(temp_app_path, exist_ok=True)

    # Define app-level folders
    app_folders = [
        "api",  # API endpoints
        "config",  # App-level configuration
        "docs",  # Documentation
        "fixtures",  # Data fixtures
        "patches",  # Patches for migrations
        "public/css",  # Public assets
        "public/js",  # JavaScript assets
        "public/images",  # Images
        "templates",  # HTML and other templates
        "tests",  # Test files
        "translations",  # Translation files
        "www",  # Web pages
    ]

    for folder in app_folders:
        folder_path = os.path.join(temp_app_path, app_name, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Create the main module folder (named after the app)
    module_path = os.path.join(temp_app_path, app_name, app_name)
    os.makedirs(module_path, exist_ok=True)

    # Define module-level folders
    module_folders = [
        "doctype",  # Custom doctypes
        "report",  # Reports
        "dashboard",  # Dashboards
        "dashboard_chart",  # Dashboard charts
        "print_format",  # Print formats
        "workspace",  # Workspaces
    ]

    for folder in module_folders:
        folder_path = os.path.join(module_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Prepare dynamic content to pass to the file creation function
    dynamic_content = {}

    if title:
        dynamic_content[
            "hooks.py"
        ] = f"""# App Information
app_name = "{app_name}"
app_title = "{title}"
app_description = "{description}"
app_publisher = "{publisher}"
app_email = "{email}"
app_license = "{license}"
"""

    # Convert app_name to title case for modules.txt
    dynamic_content["modules.txt"] = f"{app_name.replace('_', ' ').title()}\n"

    # Use the file creator utility to generate boilerplate files from templates, passing dynamic content
    templates_folder = os.path.join(PROJECT_ROOT, "blox", "templates")
    create_files_from_templates(
        temp_app_path, app_name, templates_folder, dynamic_content
    )

    # Add the app to the apps.txt configuration
    apps_txt_path = os.path.join(PROJECT_ROOT, "config", "apps.txt")
    with open(apps_txt_path, "a") as apps_file:
        apps_file.write(f"{app_name}\n")

    # Attempt to initialize a git repository
    try:
        subprocess.check_call(["git", "init"], cwd=temp_app_path)
        subprocess.check_call(["git", "checkout", "-b", "main"], cwd=temp_app_path)

        # Move the temporary directory to the final location
        shutil.move(temp_app_path, final_app_path)

        click.echo(
            f"Initialized a new Git repository with 'main' branch in '{final_app_path}'."
        )
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to initialize Git repository: {e}")
        # Rollback: Remove the temporary directory if it was created
        if os.path.exists(temp_app_path):
            shutil.rmtree(temp_app_path)
        click.echo(f"Rolled back the creation of the app '{app_name}'.")

    if os.path.exists(final_app_path):
        click.echo(f"The app '{app_name}' has been created successfully.")
    else:
        click.echo(f"Failed to create the app '{app_name}'.")

    run_migration()