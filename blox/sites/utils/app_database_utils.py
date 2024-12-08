import os
import sys
import json
import django
from pathlib import Path
import click
from ...utils.text import underscore_to_titlecase_main
from ...utils.config import DOCS_JSON_PATH

def initialize_django_env(django_path):
    """Initialize the Django environment based on django_path."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Update to your settings module
    sys.path.insert(0, django_path)  # Add Django project path to Python path
    django.setup()

def update_or_create_entry(model, id_value, name_value, **kwargs):
    """
    Update an existing entry's name if the ID exists, or create a new entry.
    
    Args:
        model: The model class to query.
        id_value: The ID to look for.
        name_value: The name to set or update.
        kwargs: Additional fields for creating a new entry.
    
    Returns:
        A tuple of (instance, created).
    """
    instance, created = model.objects.get_or_create(id=id_value, defaults={"name": name_value, **kwargs})
    if not created and instance.name != name_value:
        instance.name = name_value
        instance.save()
    return instance, created

def create_entries_from_config(django_path):
    """Process the JSON configuration file and create/update database entries."""
    # Initialize Django environment
    initialize_django_env(django_path)

    # Import models after Django setup
    from core.models import App, Module, Document  # Update with actual path to models

    # Load JSON configuration file
    with open(DOCS_JSON_PATH, "r") as file:
        config = json.load(file)

    # Process each app and its modules/documents
    for app_data in config:
        app_id = app_data["id"]
        app_name = app_data["name"]

        # Update or create the App entry
        app, _ = update_or_create_entry(App, app_id, app_name)

        for module_data in app_data.get("modules", []):
            module_id = module_data["id"]
            module_name = module_data["name"]

            # Update or create the Module entry, linked to the App
            module, _ = update_or_create_entry(
                Module, 
                module_id, 
                module_name, 
                app=app
            )

            for doc_data in module_data.get("docs", []):
                doc_id = doc_data["id"]
                doc_name = doc_data["name"]

                # Update or create the Document entry, linked to both Module and App
                update_or_create_entry(
                    Document, 
                    doc_id, 
                    doc_name, 
                    module=module, 
                    app=app
                )

