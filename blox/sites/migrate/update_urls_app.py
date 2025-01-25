import os

import click

from ...utils.config import find_module_base_path
from ...utils.text import (to_snake_case, to_titlecase_no_space)
from ..utils.app_actions import get_name_by_id


def update_urls_py(app_name, modules, django_path):
    """Update urls.py to register ViewSets for models within an app."""

    # Path to urls.py
    urls_path = os.path.join(django_path, f"{app_name}_app", "urls.py")

    # Initialize content for urls.py
    urls_content = "from django.urls import path, include\n"
    urls_content += "from rest_framework.routers import DefaultRouter\nrouter = DefaultRouter()\n"

    # Process each module
    for module in modules:
        module_snake_case = to_snake_case(module)
        _, module_path = find_module_base_path(
            app_name=app_name, module_name=module_snake_case
        )

        # Check if the module path exists
        if not module_path or not os.path.exists(module_path):
            click.echo(
                f"Module '{module}' does not exist in app '{module_path}'. Skipping..."
            )
            continue

        # Define paths for 'doc' and 'doctype' folders
        doc_path = os.path.join(module_path, "doc")
        doctype_path = os.path.join(module_path, "doctype")

        # Check for 'doc' or 'doctype' folders and process whichever exists
        if os.path.isdir(doc_path):
            models = extract_model_names(doc_path)
        elif os.path.isdir(doctype_path):
            models = extract_model_names(doctype_path)
        else:
            click.echo(
                f"No 'doc' or 'doctype' folder found for module '{module}' in app '{app_name}'."
            )
            continue

        # Add import statement for the module
        urls_content += f"from .views.{module_snake_case} import *\n"

        # Generate ViewSet registrations for each model
        for model in models:
            model_name = to_titlecase_no_space(get_name_by_id(model, "doc"))
            viewset_name = f"{model_name}ViewSet"
            urls_content += f"router.register(r'{model}', {viewset_name})\n"

    # Add the router's URLs to urlpatterns
    urls_content += """

urlpatterns = [
    path('', include(router.urls)),
]
"""

    # Write the final urls.py
    with open(urls_path, "w") as file:
        file.write(urls_content)


def extract_model_names(folder_path):
    """Extract model names based on folder contents, skipping directories
    starting with '_' or 'pycache'."""
    models = []
    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)
        if os.path.isdir(item_path) and not item_name.startswith(("_", "pycache")):
            models.append(item_name)
    return models
