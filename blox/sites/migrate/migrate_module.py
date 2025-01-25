import os

import click

from ...utils.config import find_module_base_path
from ...utils.text import to_snake_case
from .migrate_doc import migrate_doc
from .update_urls import underscore_to_titlecase


def add_init_files(folder_path):
    """Create __init__.py file importing all modules in the folder."""
    os.makedirs(folder_path, exist_ok=True)
    init_file_path = os.path.join(folder_path, "__init__.py")

    with open(init_file_path, "w+") as init_file:
        init_file.truncate(0)  # Clear the contents of the 
        # init_file.write(f"from . import *\n")

        # List all .py files except __init__.py
        files = [
            f[:-3]
            for f in os.listdir(folder_path)
            if f.endswith(".py") and f != "__init__.py"
        ]

        # Write imports for each file in snake_case and lowercase
        for file in files:
            snake_case_file = to_snake_case(file).lower()
            init_file.write(f"from .{snake_case_file} import *\n")


def underscore_to_titlecase(s):
    """Convert an underscore-separated string to title case."""
    return "".join(word.title() for word in s.split("_"))


def write_empty_view(folder_name, view_path):
    """Write a default class to the views.py file if it is empty."""
    class_name = underscore_to_titlecase(folder_name)
    with open(view_path, "w") as f:
        f.write(f"from rest_framework.response import Response\n\n")
        f.write(f"class Custom{class_name}:\n")
        f.write(f"    pass\n")


def migrate_module(app_name, module, django_path):
    """Migrate a specific module within an app by processing either the 'doc' or 'doctype' folder, whichever exists first."""

    # Convert module name to snake_case
    module_name = to_snake_case(module)
    _, module_path = find_module_base_path(app_name=app_name, module_name=module_name)

    # Check if the module path exists
    if not module_path or not os.path.exists(module_path):
        click.echo(f"Module '{module}' does not exist in app '{module_path}'. Skipping...")
        return

    # Define the paths for 'doc' and 'doctype' folders
    doc_path = os.path.join(module_path, "doc")
    doctype_path = os.path.join(module_path, "doctype")

    # Check for the 'doc' folder first, and process it if found
    if os.path.isdir(doc_path) and not doc_path.startswith(("_", "pycache")):
        process_folder_docs(app_name, module, doc_path, "doc", django_path)

    # If 'doc' folder is not found, check for the 'doctype' folder
    elif os.path.isdir(doctype_path) and not doctype_path.startswith(("_", "pycache")):
        process_folder_docs(app_name, module, doctype_path, "doctype", django_path)

    # If neither folder is found, print a message
    else:
        click.echo(
            f"No 'doc' or 'doctype' folder found for module '{module}' in app '{app_name} {module_path}'."
        )
 


STRUCTURE = {
    "views": "views",
    "models": "models",
    "filters": "filters",
    "serializers": "serializers",
    "tests": "tests",
}

def process_folder_docs(app_name, module, folder_path, folder_type, django_path):
    """Processes each document or doctype in the specified folder."""
    
    # List all documents in the folder
    folder_docs = [
        item_name
        for item_name in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, item_name)) and not item_name.startswith(("_", "pycache"))
    ]

    # Iterate over the STRUCTURE and compare files in django_path
    for key, structure_item in STRUCTURE.items():
        module_path = os.path.join(django_path, app_name, structure_item, module)
        
        if os.path.exists(module_path):
            # List all files in the structure module path
            module_files = os.listdir(module_path)
            
            for module_file in module_files:
                # Skip files starting with an underscore
                if module_file.startswith("_"):
                    continue
                
                file_base_name, _ = os.path.splitext(module_file)  # Remove file extension
                
                # Remove the file if it is not in folder_docs
                if file_base_name not in folder_docs:
                    file_to_remove = os.path.join(module_path, module_file)
                    try:
                        os.remove(file_to_remove)
                        print(f"Removed unused file: {file_to_remove}")
                    except Exception as e:
                        print(f"Error removing file {file_to_remove}: {e}")

    # Process each document in the folder
    for item_name in folder_docs:
        item_path = os.path.join(folder_path, item_name)
        
        if os.path.isdir(item_path):
            migrate_doc(
                app_name=app_name,
                module=module,
                doc=item_name,
                django_path=django_path,
            )

