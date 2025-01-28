import os
import subprocess
import sys

import click
import traceback
from ..utils.config import PROJECT_ROOT


@click.command()
def build() -> None:
    venv_path = os.path.join(PROJECT_ROOT, "env")
    if not os.path.exists(venv_path):
        click.echo("Virtual environment not found. Please run 'blox setup' first.")
        return

    python_executable = os.path.join(venv_path, "bin", "python3")
    if sys.platform.startswith("win"):
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")

    try:
        # Build Django static files
        click.echo(click.style("Building Django static files...", fg="blue"))
        subprocess.check_call(
            [python_executable, "manage.py", "collectstatic", "--noinput"],
            cwd=os.path.join(PROJECT_ROOT, "apps/core/django"),
        )
        click.echo(click.style("Django static files built successfully.", fg="green"))

        # Build Next.js project
        click.echo(click.style("Building Next.js project...", fg="blue"))
        subprocess.check_call(
            ["npm", "run", "build"], cwd=os.path.join(PROJECT_ROOT, "apps/core/nextjs")
        )
        click.echo(click.style("Next.js project built successfully.", fg="green"))

    except subprocess.CalledProcessError as e:
        click.echo(click.style(f"Build failed: {str(e)}", fg="red"))
    except Exception as e:
        click.echo(click.style(f"An unexpected error occurred: {str(e)}", fg="red"))
        exc_type, exc_value, exc_tb = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_tb)
