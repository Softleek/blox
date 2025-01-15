import os
import shutil

import click

from ...utils.config import PROJECT_ROOT
from ...sites.migrate.migrate import run_migration


@click.command()
@click.argument("app_name")
@click.argument("module_name")
def dropmodule(app_name, module_name):
    """Delete the specified module from the Django app and remove it from modules.txt."""

    # Path to the app's module directory
    app_path = os.path.join(PROJECT_ROOT, "apps", app_name)
    module_path = os.path.join(app_path, module_name)

    # Check if the app folder exists
    if not os.path.exists(app_path):
        click.echo(f"The app '{app_name}' does not exist.")
        return

    # Check if the module folder exists
    if not os.path.exists(module_path):
        click.echo(f"The module '{module_name}' does not exist in '{app_name}'.")
        return

    # Attempt to remove the module directory
    try:
        shutil.rmtree(module_path)
    except Exception as e:
        click.echo(f"An error occurred while trying to delete the module: {e}")
        return

    # Remove the module from modules.txt
    modules_txt_path = os.path.join(app_path, "modules.txt")
    try:
        with open(modules_txt_path, "r") as modules_file:
            modules = modules_file.readlines()

        with open(modules_txt_path, "w") as modules_file:
            for line in modules:
                if line.strip() != module_name:
                    modules_file.write(line)

        click.echo(f"The module '{module_name}' has been removed.")
    except Exception as e:
        click.echo(f"Failed to update modules.txt: {e}")
    run_migration()
