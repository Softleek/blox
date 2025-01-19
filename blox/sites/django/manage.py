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
def django(command, args, site=None):
    """Run Django management commands."""
    django_path = os.path.join(
        PROJECT_ROOT, "sites", "django"
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


if __name__ == "__main__":
    django()
