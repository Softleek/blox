import os
import re
import subprocess
from typing import List
from urllib.parse import urlparse

import click

from ..sites.utils.installdjangoapp import install_django_app
from ..utils.config import PROJECT_ROOT
from ..utils.run_process import get_python_executable, run_subprocess
from ..utils.text import to_snake_case


def remove_hiredis_from_toml() -> None:
    """
    Remove any lines containing 'hiredis' from any .toml files in the project.
    """
    for root, _, files in os.walk(PROJECT_ROOT):
        for file in files:
            if file.endswith(".toml"):
                toml_path = os.path.join(root, file)
                with open(toml_path, "r") as toml_file:
                    lines = toml_file.readlines()

                filtered_lines: List[str] = [
                    line for line in lines if "hiredis" not in line
                ]

                if len(filtered_lines) != len(lines):
                    with open(toml_path, "w") as toml_file:
                        toml_file.writelines(filtered_lines)


@click.command()
@click.argument("git_url")
@click.argument("name", required=False)
def getapp(git_url: str, name: str = None) -> None:
    """
    Clone a Django app from a Git repository using the provided URL and optional app name.

    Args:
        git_url (str): The URL of the Git repository to clone.
        name (str): The name of the app to be used. If not provided, it will be parsed from the git_url.
    """
    if name:
        app_name = name
    else:
        parsed_url = urlparse(git_url)
        repo_name = os.path.basename(parsed_url.path).replace(".git", "")
        app_name = to_snake_case(repo_name)

    target_dir = os.path.join(PROJECT_ROOT, "apps", app_name)

    if os.path.exists(target_dir):
        click.echo(f"The app '{app_name}' already exists in the directory.")
        return

    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", git_url, target_dir], check=True
        )
        click.echo(f"The app '{app_name}' has been cloned from '{git_url}'.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to clone the repository: {e}")

    remove_hiredis_from_toml()

    apps_txt_path = os.path.join(PROJECT_ROOT, "config", "apps.txt")
    with open(apps_txt_path, "a") as apps_file:
        apps_file.write(f"{app_name}\n")

    run_subprocess(
        [get_python_executable(), "pip", "install", f"apps/{app_name}"],
        cwd=PROJECT_ROOT,
    )

    install_django_app(app_name, PROJECT_ROOT)
