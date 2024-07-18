import os


def find_project_root(current_path):
    while current_path != '/':
        if 'blox.config' in os.listdir(current_path):
            return current_path
        current_path = os.path.dirname(current_path)
    raise FileNotFoundError("Project root with 'blox.config' not found.")


PROJECT_ROOT = find_project_root(os.getcwd())
SETTINGS_PATH = os.path.join(
    PROJECT_ROOT, 'apps/core/django/backend/settings.py')
BASE_PATH = os.path.join(
    PROJECT_ROOT, 'apps/core/django')

APPS_TXT_PATH = os.path.join(PROJECT_ROOT, 'config', 'apps.txt')
CUSTOM_APPS_PATH = os.path.join(PROJECT_ROOT, 'apps', 'custom')
