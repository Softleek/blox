import os
import click
import json
from ...utils.config import DOCS_JSON_PATH, find_module_base_path
from ...utils.text import to_snake_case
from .app_actions import find_modules
from .load_doc_config import load_existing_data


def process_docs(folder_path):
    """Processes all documents in the specified folder and returns a list of document names."""
    docs = []
    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)
        if os.path.isdir(item_path):  # Only process directories (docs)
            # Construct the expected JSON file path
            json_file_path = os.path.join(item_path, f"{item_name}.json")
            doc_name = item_name  # Default to the folder name

            # Check if the JSON file exists and load the 'name' field if present
            if os.path.isfile(json_file_path):
                try:
                    with open(json_file_path, 'r') as json_file:
                        data = json.load(json_file)
                        doc_name = data.get('name', item_name)  # Fallback to folder name if 'name' not found
                except (json.JSONDecodeError, IOError):
                    click.echo(f"Error reading or parsing JSON file: {json_file_path}. Using folder name.")

            # Create doc data
            doc_data = {
                "id": to_snake_case(item_name),  # Convert doc name to snake_case for ID
                "name": doc_name  # Use the name from JSON or folder name
            }
            docs.append(doc_data)
    return docs


def save_data_to_file(data):
    """Saves the updated data back to the JSON file."""
    with open(DOCS_JSON_PATH, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def find_or_create_app_entry(existing_data, app_id, app_name):
    """Finds an app entry by ID or creates a new one, always replacing the name if found."""
    app_entry = next((app for app in existing_data if app["id"] == app_id), None)
    if not app_entry:
        app_entry = {"id": app_id, "name": app_name, "modules": []}
        existing_data.append(app_entry)
    else:
        app_entry["name"] = app_name  # Always replace the name
    return app_entry


def find_or_create_module_entry(app_entry, module_id, module_name):
    """Finds a module entry by ID within an app or creates a new one, always replacing the name if found."""
    module_entry = next((mod for mod in app_entry["modules"] if mod["id"] == module_id), None)
    if not module_entry:
        module_entry = {"id": module_id, "name": module_name, "docs": []}
        app_entry["modules"].append(module_entry)
    else:
        module_entry["name"] = module_name  # Always replace the name
    return module_entry


def update_module_docs(module_entry, docs):
    """Updates the documents in a module, replacing names if IDs match."""
    for doc in docs:
        existing_doc = next((d for d in module_entry["docs"] if d["id"] == doc["id"]), None)
        if existing_doc:
            existing_doc["name"] = doc["name"]  # Replace the name if ID matches
        else:
            module_entry["docs"].append(doc)


def add_single_doc(app_id, app_name, module_id, module_name, doc_id, doc_name):
    """Adds or updates a single document in the specified app and module."""
    # Load existing data
    existing_data = load_existing_data()

    # Find or create the app entry
    app_entry = find_or_create_app_entry(existing_data, app_id, app_name)

    # Find or create the module entry
    module_entry = find_or_create_module_entry(app_entry, module_id, module_name)

    # Check if the document exists
    doc_entry = next((doc for doc in module_entry["docs"] if doc["id"] == doc_id), None)
    if doc_entry:
        # Replace the name even if the ID matches
        doc_entry["name"] = doc_name
    else:
        # Add new document if it doesn't exist
        doc_entry = {"id": doc_id, "name": doc_name}
        module_entry["docs"].append(doc_entry)
        click.echo(f"Document '{doc_name}' added to module '{module_name}' in app '{app_name}'.")

    # Save the updated data
    save_data_to_file(existing_data)


def process_module(app_name, module, app_entry):
    """Processes a module, updates its docs, and appends it to the app entry."""
    module_id = to_snake_case(module)
    module_name = module

    _, module_path = find_module_base_path(app_name=app_name, module_name=module_id)

    # Check if module path exists
    if not module_path or not os.path.exists(module_path):
        click.echo(f"Module '{module}' does not exist in app '{app_name}'. Skipping...")
        return

    # Define paths for 'doc' and 'doctype' folders
    doc_path = os.path.join(module_path, module_id, "doc")
    doctype_path = os.path.join(module_path, module_id, "doctype")

    docs = []
    # Check for the 'doc' or 'doctype' folder and process whichever exists
    if os.path.isdir(doc_path):
        docs = process_docs(doc_path)
    elif os.path.isdir(doctype_path):
        docs = process_docs(doctype_path)

    # Find or create the module entry
    module_entry = find_or_create_module_entry(app_entry, module_id, module_name)

    # Update the module docs
    update_module_docs(module_entry, docs)


def create_doctypes_json(app_name):
    """Generates or updates the doctypes.json file for the app with its modules and docs."""

    # Load existing data
    existing_data = load_existing_data()

    # Find or create the app entry
    app_id = to_snake_case(app_name)
    app_entry = find_or_create_app_entry(existing_data, app_id, app_name)

    # Process each module in the app
    modules = find_modules(app_name)  # Assumes this function exists and lists the app's modules
    for module in modules:
        process_module(app_name, module, app_entry)

    # Save the updated data
    save_data_to_file(existing_data)



def add_single_entry(app_name=None, module_name=None, doc_name=None):
    """Allows adding a single doc, module, or app."""
    app_id = to_snake_case(app_name) if app_name else None
    module_id = to_snake_case(module_name) if module_name else None
    doc_id = to_snake_case(doc_name) if doc_name else None

    existing_data = load_existing_data()

    if app_name and module_name and doc_name:
        add_single_doc(app_id, app_name, module_id, module_name, doc_id, doc_name)
    elif app_name and module_name:
        app_entry = find_or_create_app_entry(existing_data, app_id, app_name)
        find_or_create_module_entry(app_entry, module_id, module_name)
        save_data_to_file(existing_data)
    elif app_name:
        find_or_create_app_entry(existing_data, app_id, app_name)
        click.echo(f"App '{app_name}' updated or added.")
        save_data_to_file(existing_data)
    else:
        click.echo("Invalid parameters provided.")
