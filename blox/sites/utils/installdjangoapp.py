import os
import json
import subprocess
import sys
from .module_structure import create_module_structure  # Importing the logic

def activate_virtualenv(project_root):
    """Return the path to the activate script of the virtual environment."""
    if sys.platform.startswith('win'):
        return os.path.join(project_root, 'env', 'Scripts', 'activate')
    return os.path.join(project_root, 'env', 'bin', 'activate')

def get_python_executable(project_root):
    """Return the path to the Python executable in the virtual environment."""
    venv_path = os.path.join(project_root, 'env')
    if sys.platform.startswith('win'):
        return os.path.join(venv_path, 'Scripts', 'python.exe')
    return os.path.join(venv_path, 'bin', 'python')

def install_django_app(site, app, project_root):
    """Create a Django app in a selected site using the Django startapp command."""
    app_name = f"{app}_app"
    
    # Define paths
    sites_json_path = os.path.join(project_root, 'config', 'sites.json')
    site_path = os.path.join(project_root, 'sites', site)
    django_path = os.path.join(site_path, "django")

    # Load site options
    with open(sites_json_path, 'r') as sites_file:
        sites = json.load(sites_file)

    # Check if the site exists
    if not any(s['site_name'] == site for s in sites):
        raise ValueError(f"Site '{site}' does not exist.")

    if not os.path.exists(site_path):
        raise ValueError(f"Path for site '{site}' does not exist.")

    # Load app options from apps.txt
    apps_txt_path = os.path.join(project_root, 'config', 'apps.txt')
    with open(apps_txt_path, 'r') as apps_file:
        apps = [line.strip() for line in apps_file if line.strip() and not line.startswith('#')]

    # if app in apps:
    #     raise ValueError(f"App '{app}' already exists in the available apps list.")

    # Determine Python executable
    python_executable = get_python_executable(project_root)

    # Run Django's startapp command
    try:
        # Activate the virtual environment and run the command
        command = [python_executable, 'manage.py', 'startapp', app_name]
        subprocess.check_call(command, cwd=django_path)
        print(f"App '{app}' has been created successfully in site '{site}'.")

        # Update INSTALLED_APPS in settings.py
        settings_path = os.path.join(django_path, 'backend', 'settings.py')  # Adjust path as necessary
        with open(settings_path, 'r') as file:
            settings_content = file.readlines()

        installed_apps_index = None
        for i, line in enumerate(settings_content):
            if "INSTALLED_APPS = [" in line:
                installed_apps_index = i
                break

        if installed_apps_index is not None:
            end_index = installed_apps_index
            while not settings_content[end_index].strip().endswith("]"):
                end_index += 1
            settings_content.insert(end_index, f"    '{app_name}',\n")
            
        path_append_line = f"sys.path.append(str(os.path.join(PROJECT_PATH, \"apps\", \"{app}\")))"
        if path_append_line not in settings_content:
            settings_content.append(f"\n{path_append_line}")

        with open(settings_path, "w") as settings_file:
            settings_file.writelines(settings_content)

      
        # Create urls.py for the new app
        app_path = os.path.join(django_path, app_name)
        custom_app_path = os.path.join(project_root, 'apps', app )
        urls_path = os.path.join(app_path, "urls.py")
        with open(urls_path, "w") as urls_file:
            urls_file.write("from django.urls import path\n\n")
            urls_file.write("urlpatterns = [\n")
            urls_file.write("    # Define your app's URLs here\n")
            urls_file.write("]\n")

        # Add the new app's URL to project's urls.py
        main_urls_path = os.path.join(django_path, "core", "urls.py")  # Adjust path as necessary
        with open(main_urls_path, "a") as main_urls_file:
            main_urls_file.write("urlpatterns += [")
            main_urls_file.write(f"path('{app}/', include('{app_name}.urls')),")
            main_urls_file.write("]\n")


         # Create module structure
     # Example modules
        create_module_structure(app_path, custom_app_path,app)

    except subprocess.CalledProcessError as e:
        print(f"Failed to create the app '{app}' in site '{site}': {e}")

