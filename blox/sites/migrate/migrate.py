import json
import os
import re
import subprocess
import sys

import click

from ...utils.config import (DEFAULT_SITE, DJANGO_PATH, PROJECT_ROOT, find_django_path)
from ..utils.app_database_utils import create_entries_from_config
from ..utils.configure_app import configure_app, configure_doc, configure_module
from .migrate_app import migrate_app
from .migrate_doc import migrate_doc
from .migrate_module import migrate_module
from ...utils.file_operations import ensure_file_exists
# from ....sites.pos2.django.core.management.commands.migrate_fixtures import migrate_fixtures

MODULES_FOLDER = {
    "views": "views",
    "models": "models",
    "filters": "filters",
    "serializers": "serializers",
    "tests": "tests",
}


def remove_class_block(file_path, class_name):
    """Remove the class definition block for a specified class from a file.

    Args:
        file_path (str): Path to the file from which the class block is removed.
        class_name (str): Name of the class to remove.
    """
    with open(file_path, "r") as file:
        content = file.read()

    pattern = re.compile(rf"class {class_name}\s*\(.*?\):.*?(?=\nclass |$)", re.DOTALL)
    content = pattern.sub("", content)

    with open(file_path, "w") as file:
        file.write(content)



def updatefiles(app=None, module=None, doc=None, site=None, all=True):
    # Load sites from sites.json
    selected_site = None
    sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")
    ensure_file_exists(sites_json_path, initial_data=[])
    if os.path.exists(sites_json_path):
        with open(sites_json_path, "r") as json_file:
            sites = json.load(json_file)
    else:
        click.echo("No sites found in sites.json.")
        return

    # If --all is passed, iterate over all sites
    if all:
        for site_entry in sites:
            # Migrate all apps for the site
            installed_apps = site_entry.get("installed_apps", [])
            for app in installed_apps:
                configure_app(app)

            for app in installed_apps:
                migrate_app(app, DJANGO_PATH)

        return

    # Prompt for site if not provided
    if not site:
        selected_site = DEFAULT_SITE

    # Perform migrations based on provided options
    if doc and module and app:
        configure_doc(app, module, doc)
        migrate_doc(app, module, doc, DJANGO_PATH)
    elif module and app:
        configure_module(app, module)
        migrate_module(app, module, DJANGO_PATH)
    elif app:
        configure_app(app)
        migrate_app(app, DJANGO_PATH)
    elif selected_site:
        installed_apps = selected_site.get("installed_apps", [])
        for app in installed_apps:
            configure_app(app)
        for app in installed_apps:
            migrate_app(app, DJANGO_PATH)

    # Run Django migrations
    # create_entries_from_config(DJANGO_PATH)create_entries_from_config(DJANGO_PATH)

    subprocess.run(
        ["autoflake", "--in-place", "--remove-unused-variables",  "--recursive", "--exclude", "*/__init__.py", "."],
        cwd=DJANGO_PATH,
    )
    
    subprocess.run(
        ["autoflake", "--in-place", "--remove-all-unused-imports",  "--recursive", "--exclude", "*/__init__.py", "."],
        cwd=DJANGO_PATH,
    )

    click.echo("Migration process completed successfully.")


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
def migrate_django():
    """Execute Django migration commands (makemigrations and migrate) for a specified project.

    Args:
        skip_updatefiles (bool): If True, skips calling updatefiles before migrations.
    """
    run_migrate_django()
    
    
def run_migrate_django(site=None):
    """Run Django makemigrations and migrate commands."""
    python_executable = get_python_executable()

    # Prepare database argument if site is provided
    db_arg = [f"--database={site}"] if site else []

    # Run makemigrations
    subprocess.run(
        [python_executable, "manage.py", "makemigrations"],
        cwd=DJANGO_PATH,
    )

    # Run migrate
    subprocess.run(
        [python_executable, "manage.py", "migrate", "--noinput"] + db_arg,
        cwd=DJANGO_PATH,
    )

    create_entries_from_config(DJANGO_PATH)
    

def run_migration(app=None, module=None, doc=None, site=None, all_sites=False, skip=False):
    """Core migration process."""
    import traceback

    try:
        if not skip:
            updatefiles(app, module, doc, site, all_sites)
        run_migrate_django(site)
        click.echo("Migration completed successfully.")
    except Exception as e:
        click.echo(f"Migration failed: {e}")
        exc_type, exc_value, exc_tb = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_tb)


@click.command()
@click.option("--app", default=None, help="Specify an app to migrate.")
@click.option(
    "--module", default=None, help="Specify a module to migrate. Requires --app."
)
@click.option(
    "--doc",
    default=None,
    help="Specify a document to migrate. Requires --app and --module.",
)
@click.option(
    "--site",
    default=None,
    help="Specify a site to migrate. If not provided, prompts for a site.",
)
@click.option("-a", "--all", is_flag=True, help="Migrate all sites.")
@click.option(
    "-s", "--skip", is_flag=True, help="Skip updating files before running migrations."
)
def migrate(app=None, module=None, doc=None, site=None, all=False, skip=False):
    """Run Django makemigrations and migrate commands."""
    run_migration(app, module, doc, site, all, skip)


@click.command()
@click.option(
    "--site",
    default=None,
    help="Specify a site to migrate. If not provided, prompts for a site.",
)
def registermodels(site):
    """Run Django makemigrations and migrate commands."""
    create_entries_from_config(find_django_path(site))