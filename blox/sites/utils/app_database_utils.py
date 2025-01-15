import json
import os
import sys

import django

from ...utils.config import DOCS_JSON_PATH


def initialize_django_env(django_path):
    """Initialize the Django environment based on django_path."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "backend.settings"
    )  # Update to your settings module
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
    instance, created = model.objects.get_or_create(
        id=id_value, defaults={"name": name_value, **kwargs}
    )
    if not created and instance.name != name_value:
        instance.name = name_value
        instance.save()
    return instance, created


def create_entries_from_config(django_path):
    """Process the JSON configuration file and create/update database entries."""
    # Initialize Django environment
    initialize_django_env(django_path)

    # Import models after Django setup
    from core.models import (App,  # Update with actual path to models
                             Document, Module)

    # Load JSON configuration file
    with open(DOCS_JSON_PATH, "r") as file:
        config = json.load(file)

    # Cache existing entries to reduce redundant queries
    existing_apps = {app.id: app for app in App.objects.all()}
    existing_modules = {module.id: module for module in Module.objects.all()}
    existing_docs = {doc.id: doc for doc in Document.objects.all()}

    # Prepare lists for bulk operations
    apps_to_create = []
    modules_to_create = []
    docs_to_create = []

    # Process each app and its modules/documents
    for app_data in config:
        app_id = app_data["id"]
        app_name = app_data["name"]

        # Update or create the App entry
        if app_id in existing_apps:
            app = existing_apps[app_id]
            if app.name != app_name:
                app.name = app_name
                app.save()
        else:
            apps_to_create.append(App(id=app_id, name=app_name))

        # Process modules and documents similarly
        for module_data in app_data.get("modules", []):
            module_id = module_data["id"]
            module_name = module_data["name"]

            if module_id in existing_modules:
                module = existing_modules[module_id]
                if module.name != module_name:
                    module.name = module_name
                    module.save()
            else:
                modules_to_create.append(
                    Module(id=module_id, name=module_name, app_id=app_id)
                )

            for doc_data in module_data.get("documents", []):
                doc_id = doc_data["id"]
                doc_name = doc_data["name"]

                if doc_id in existing_docs:
                    doc = existing_docs[doc_id]
                    if doc.name != doc_name:
                        doc.name = doc_name
                        doc.save()
                else:
                    docs_to_create.append(
                        Document(id=doc_id, name=doc_name, module_id=module_id)
                    )

    # Bulk create new entries
    if apps_to_create:
        App.objects.bulk_create(apps_to_create)
    if modules_to_create:
        Module.objects.bulk_create(modules_to_create)
    if docs_to_create:
        Document.objects.bulk_create(docs_to_create)
