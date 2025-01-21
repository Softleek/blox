import json
import os
import subprocess
import sys


def get_python_executable(project_root):
    """Return the path to the Python executable in the virtual environment."""
    venv_path = os.path.join(project_root, "env")
    if sys.platform.startswith("win"):
        return os.path.join(venv_path, "Scripts", "python.exe")
    return os.path.join(venv_path, "bin", "python")


def remove_app_from_installed_apps(app, app_name, settings_path):
    """Remove the app from INSTALLED_APPS and sys.path in the settings.py."""

    with open(settings_path, "r") as file:
        settings_content = file.readlines()

    # Find the installed apps section
    installed_apps_index = None
    for i, line in enumerate(settings_content):
        if "INSTALLED_APPS = [" in line:
            installed_apps_index = i
            break

    if installed_apps_index is None:
        raise ValueError("Could not find INSTALLED_APPS in the settings file.")

    # Remove the app from the INSTALLED_APPS list and sys.path.append
    updated_settings = []
    app_found = False
    path_app_found = False
    for line in settings_content:
        # Remove the app from INSTALLED_APPS
        if line.strip() == f"'{app_name}'," or line.strip() == f'"{app_name}",':
            app_found = True
            continue  # Skip this line (removing the app)

        # Remove both single and double quotes sys.path.append lines for the app
        if (
            f"sys.path.append(str(os.path.join(PROJECT_PATH, 'apps', '{app}')))" in line
            or f'sys.path.append(str(os.path.join(PROJECT_PATH, "apps", "{app}")))'
            in line
        ):
            path_app_found = True
            continue  # Skip this line (removing sys.path.append)

        updated_settings.append(line)

    # Write changes back to settings.py if any changes were made
    if app_found or path_app_found:
        with open(settings_path, "w") as settings_file:
            settings_file.writelines(updated_settings)

        if app_found:
            print(f"App '{app}' has been removed from INSTALLED_APPS.")
        if path_app_found:
            print(f"sys.path.append for '{app}' has been removed.")
    else:
        print(f"App '{app}' or its sys.path.append entry was not found.")


def remove_app_urls(app, app_name, urls_path):
    """Remove the app's URL pattern from the project's main urls.py."""
    with open(urls_path, "r") as file:
        urls_content = file.readlines()

    # Remove the app's URL entry
    updated_urls = []
    app_found = False
    for line in urls_content:
        if f"path('{app}/', include('{app_name}.urls'))," in line:
            app_found = True
            continue  # Skip this line (removing the URL entry)
        updated_urls.append(line)

    if app_found:
        with open(urls_path, "w") as urls_file:
            urls_file.writelines(updated_urls)
        print(f"URLs for app '{app}' have been removed.")
    else:
        print(f"No URL entry found for app '{app}'.")


def uninstall_django_app(site, app, project_root):
    """Uninstall a Django app from a selected site by reversing actions taken during installation."""
    app_name = f"{app}_app"
    # Define paths
    sites_json_path = os.path.join(project_root, "sites", "sites.json")
    site_path = os.path.join(project_root, "sites", site)
    django_path = os.path.join(site_path, "django")

    # Load site options
    with open(sites_json_path, "r") as sites_file:
        sites = json.load(sites_file)

    # Check if the site exists
    if not any(s["site_name"] == site for s in sites):
        raise ValueError(f"Site '{site}' does not exist.")

    if not os.path.exists(site_path):
        raise ValueError(f"Path for site '{site}' does not exist.")

    # Determine Python executable
    get_python_executable(project_root)

    # Check if app exists in the site
    app_path = os.path.join(django_path, app_name)
    if not os.path.exists(app_path):
        raise ValueError(f"App '{app}' does not exist in the site '{site}'.")

    # Remove the app's entry in settings.py
    settings_path = os.path.join(
        django_path, "backend", "settings.py"
    )  # Adjust path as necessary
    remove_app_from_installed_apps(app, app_name, settings_path)

    # Remove the app's URL from the project's main urls.py
    main_urls_path = os.path.join(
        django_path, "core", "urls.py"
    )  # Adjust path as necessary
    remove_app_urls(app, app_name, main_urls_path)

    # Simulate removing the app directory
    try:
        if os.name == "nt":  # Windows
            subprocess.check_call(["cmd", "/c", "rmdir", "/s", "/q", app_path])
        else:  # Unix-based systems
            subprocess.check_call(["rm", "-rf", app_path])
        print(f"App '{app}' has been removed from site '{site}'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to remove the app '{app}' from site '{site}': {e}")

    # You can also remove the app from the apps.txt file if necessary (optional).
