import os
import shutil
import click
import subprocess
from ..utils.config import PROJECT_ROOT
from ..utils.subprocess import run_subprocess


@click.command()
@click.argument("app_name")
def newapp(app_name):
    """Create a new Django app with the specified name."""

    # Define paths
    temp_app_path = os.path.join(PROJECT_ROOT, "apps", f"temp_{app_name}")
    final_app_path = os.path.join(PROJECT_ROOT, "apps", app_name)

    # Check if the app already exists in INSTALLED_APPS
    new_installed_app = f"'{app_name}',"
    apps_txt_path = os.path.join(PROJECT_ROOT, "config", "apps.txt")
    with open(apps_txt_path, "r") as settings_file:
        settings = settings_file.readlines()

    if any(new_installed_app.strip().strip(",") in line for line in settings):
        click.echo(f"The app '{app_name}' is already in INSTALLED_APPS.")
        return

    # Create the custom app folder and required files in the temporary path
    os.makedirs(temp_app_path, exist_ok=True)

    # Create an empty __init__.py file in the main app folder
    init_file_path = os.path.join(temp_app_path, "__init__.py")
    open(init_file_path, "w").close()

    # Create the app subfolders
    subfolders = [
        "api",
        "fixtures",
        os.path.join(app_name, "doc"),
        os.path.join(app_name, "dashboard"),
        os.path.join(app_name, "report"),
        os.path.join(app_name, "script"),
    ]

    for subfolder in subfolders:
        folder_path = os.path.join(temp_app_path, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        # Create an empty __init__.py file in each subfolder
        init_file_path = os.path.join(folder_path, "__init__.py")
        open(init_file_path, "w").close()

    # Create additional necessary files
    with open(os.path.join(temp_app_path, "modules.txt"), "w") as modules_file:
        modules_file.write(f"# List of modules for {app_name}\n")
        modules_file.write(f"{app_name}\n")
    with open(os.path.join(temp_app_path, "requirements.txt"), "w") as requirements_file:
        requirements_file.write("# List of requirements\n")
    with open(os.path.join(temp_app_path, "package.json"), "w") as package_file:
        package_file.write(
            '{\n    "name": "' + app_name + '",\n    "version": "1.0.0",\n    "main": "index.js",\n    "scripts": {\n        "start": ""\n    }\n}\n'
        )

    # Attempt to initialize a git repository
    try:
        # Run 'git init' without activating the virtual environment first
        subprocess.check_call(["git", "init"], cwd=temp_app_path)
        subprocess.check_call(["git", "checkout", "-b", "main"], cwd=temp_app_path)

        # Move the temporary directory to the final location
        shutil.move(temp_app_path, final_app_path)

        # Add the new app to apps.txt
        with open(apps_txt_path, "a") as apps_file:
            apps_file.write(f"{app_name}\n")

        click.echo(f"Initialized a new Git repository with 'main' branch in '{final_app_path}'.")
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
