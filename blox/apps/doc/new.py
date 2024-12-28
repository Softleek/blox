import os
import click
import re
from ...utils.config import PROJECT_ROOT
from .file_handler import create_files
from ...utils.text import to_snake_case

@click.command()
@click.argument("doc_name")
@click.option("--app", type=str, help="Select the app by number or name.")
@click.option("--module", type=str, help="Select the module by number or name.")
def newdoc(doc_name, app, module):
    """Create a new documentation folder with default files in the specified module."""

    # Convert inputs to snake_case
    doc_name = to_snake_case(doc_name)
    app = to_snake_case(app) if app else None
    module = to_snake_case(module) if module else None

    # Load available apps
    apps_txt_path = os.path.join(PROJECT_ROOT, "config", "apps.txt")
    apps = []
    with open(apps_txt_path, "r") as f:
        apps = [to_snake_case(line.strip()) for line in f if line.strip() and not line.startswith("#")]

    if not apps:
        click.echo("No apps found.")
        return

    # Determine app selection
    if app is None:
        click.echo("Select an app:")
        for i, app_name in enumerate(apps):
            click.echo(f"{i + 1}: {app_name}")
        app_choice = click.prompt("Enter the number of the app or the app name", type=str)
        if app_choice.isdigit():
            app_index = int(app_choice) - 1
            selected_app = apps[app_index] if 0 <= app_index < len(apps) else None
        else:
            selected_app = to_snake_case(app_choice) if to_snake_case(app_choice) in apps else None
    else:
        selected_app = app if app in apps else None

    if selected_app is None:
        click.echo("Invalid app selection.")
        return

    # Load available modules for the selected app
    module_txt_path = os.path.join(PROJECT_ROOT, "apps", selected_app, selected_app, "modules.txt")
    modules = []
    with open(module_txt_path, "r") as f:
        modules = [to_snake_case(line.strip()) for line in f if line.strip() and not line.startswith("#")]

    if not modules:
        click.echo(f"No modules found for app '{selected_app}'.")
        return

    # Determine module selection
    if module is None:
        click.echo("Select a module:")
        for i, module_name in enumerate(modules):
            click.echo(f"{i + 1}: {module_name}")
        module_choice = click.prompt("Enter the number of the module or the module name", type=str)
        if module_choice.isdigit():
            module_index = int(module_choice) - 1
            selected_module = modules[module_index] if 0 <= module_index < len(modules) else None
        else:
            selected_module = to_snake_case(module_choice) if to_snake_case(module_choice) in modules else None
    else:
        selected_module = module if module in modules else None

    if selected_module is None:
        click.echo("Invalid module selection.")
        return

    # Define paths
    module_path = os.path.join(PROJECT_ROOT, "apps", selected_app, selected_app, selected_module)
    created_folder = create_files(module_path, doc_name)

    click.echo(f"The documentation folder '{doc_name}' has been created successfully in '{selected_module}'.")
