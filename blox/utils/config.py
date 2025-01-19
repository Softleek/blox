import json
import os

import click

from .default_site import get_default_site_info
from ..utils.file_operations import ensure_file_exists

def find_project_root(current_path):
    while current_path != "/":
        if "blox.config" in os.listdir(current_path):
            return current_path
        current_path = os.path.dirname(current_path)
    raise FileNotFoundError("Project root with 'blox.config' not found.")


def find_django_path(site):
    return os.path.join(PROJECT_ROOT, f"sites/{site}/django")


def write_running_ports(django_port, nextjs_port):
    next_path = os.path.join(PROJECT_ROOT, "sites", "nextjs")
    env_file_path = os.path.join(next_path, ".env.local")

    # Update the .env.local file
    if not os.path.exists(env_file_path):
        with open(env_file_path, "w") as f:
            f.write(f"NEXT_PUBLIC_DJANGO_PORT={django_port}\n")
            f.write(f"NEXT_PUBLIC_NEXTJS_PORT={nextjs_port}\n")
    else:
        with open(env_file_path, "r") as f:
            lines = f.readlines()

        with open(env_file_path, "w") as f:
            updated = False
            for line in lines:
                if line.startswith("NEXT_PUBLIC_DJANGO_PORT="):
                    f.write(f"NEXT_PUBLIC_DJANGO_PORT={django_port}\n")
                    updated = True
                elif line.startswith("NEXT_PUBLIC_NEXTJS_PORT="):
                    f.write(f"NEXT_PUBLIC_NEXTJS_PORT={nextjs_port}\n")
                    updated = True
                else:
                    f.write(line)

            if not updated:
                f.write(f"NEXT_PUBLIC_DJANGO_PORT={django_port}\n")
                f.write(f"NEXT_PUBLIC_NEXTJS_PORT={nextjs_port}\n")



def find_module_base_path(app_name=None, module_name=None, app_path=None):
    """Locate the modules.txt file and determine the base path for modules, searching specified directories.

    Args:
        app_name (str): Name of the app to search within.
        module_name (str, optional): Specific module name to look for within the app. Defaults to None.
        app_path (str, optional): Path to the app directory. If not provided, defaults to APPS_PATH/app_name.

    Returns:
        tuple: Path to modules.txt and the base directory for modules, or (None, None) if not found.
    """
    # Determine the base path for the app, defaults to APPS_PATH/app_name
    base_path = app_path if app_path else os.path.join(APPS_PATH, app_name)

    # First, check for modules.txt directly in the base_path
    modules_file_path = os.path.join(base_path, "modules.txt")
    if os.path.isfile(modules_file_path):
        if module_name:
            # Check if the specific module_name is listed in modules.txt
            with open(modules_file_path, "r") as modules_file:
                if module_name in [line.strip() for line in modules_file.readlines()]:
                    return modules_file_path, base_path
        else:
            # Return the modules.txt found if no module_name is specified
            return modules_file_path, base_path

    # If not found, check in the subfolder named after the app_name
    subfolder_path = os.path.join(base_path, app_name)

    if os.path.isdir(subfolder_path):
        # List all files in the subfolder
        for item in os.listdir(subfolder_path):
            if item == "modules.txt":
                modules_file_path = os.path.join(subfolder_path, item)

                return modules_file_path, subfolder_path

    return None, None


PROJECT_ROOT = find_project_root(os.getcwd())
SETTINGS_PATH = os.path.join(PROJECT_ROOT, "apps/core/django/backend/settings.py")
DB_PATH = os.path.join(PROJECT_ROOT, "apps/core/django/db.sqlite3")
BASE_PATH = os.path.join(PROJECT_ROOT, "apps/core/django")
JSON_FILE_PATH = os.path.join(PROJECT_ROOT, "apps/core/django/data.json")
NEXTJS_PATH = os.path.join(PROJECT_ROOT, "apps/core/nextjs")
APPS_TXT_PATH = os.path.join(PROJECT_ROOT, "config", "apps.txt")
SITES_JSON_PATH = os.path.join(PROJECT_ROOT, "config", "sites.json")
DOCS_JSON_PATH = os.path.join(PROJECT_ROOT, "config", "doctypes.json")
APPS_PATH = os.path.join(PROJECT_ROOT, "apps")
DJANGO_PATH =  os.path.join(PROJECT_ROOT, "sites", "django")
DEFAULT_SITE = get_default_site_info(PROJECT_ROOT)
SITES_PATH = os.path.join(PROJECT_ROOT, "sites")
