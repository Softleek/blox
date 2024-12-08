import os
import shutil
import click
from ...utils.config import PROJECT_ROOT

@click.command()
@click.argument("app_name")
@click.argument("module_name")
def newmodule(app_name, module_name):
    """Create a new module within the specified Django app."""
    
    # Path to the app's module directory
    app_path = os.path.join(PROJECT_ROOT, "apps", app_name)
    module_path = os.path.join(app_path, module_name)

    # Check if the app folder exists
    if not os.path.exists(app_path):
        click.echo(f"The app '{app_name}' does not exist.")
        return

    # Check if the module already exists
    if os.path.exists(module_path):
        click.echo(f"The module '{module_name}' already exists in '{app_name}'.")
        return

    # Create the module folder
    os.makedirs(module_path, exist_ok=True)

    # Create an empty __init__.py file in the module folder
    init_file_path = os.path.join(module_path, "__init__.py")
    open(init_file_path, "w").close()

    # Create necessary subfolders for the module
    subfolders = [
        os.path.join("doc"),
        os.path.join("dashboard"),
        os.path.join("report"),
        os.path.join("script"),
    ]

    for subfolder in subfolders:
        folder_path = os.path.join(module_path, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        # Create an empty __init__.py file in each subfolder
        init_file_path = os.path.join(folder_path, "__init__.py")
        open(init_file_path, "w").close()

    # Update modules.txt for the app
    modules_txt_path = os.path.join(app_path, "modules.txt")
    try:
        with open(modules_txt_path, "a") as modules_file:
            modules_file.write(f"{module_name}\n")
        click.echo(f"The module '{module_name}' has been created successfully in '{app_name}'.")
    except Exception as e:
        click.echo(f"Failed to update modules.txt: {e}")
        # Rollback: Remove the module if there was an error
        if os.path.exists(module_path):
            shutil.rmtree(module_path)
        click.echo(f"Rolled back the creation of the module '{module_name}'.")

