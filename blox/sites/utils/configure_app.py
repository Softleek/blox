import os
import click
from ...utils.config import find_module_base_path, DJANGO_PATH
from ...utils.text import to_snake_case, underscore_to_titlecase
from ...utils.register_models import register_to_model_json
import importlib
from .app_actions import find_modules
import json
from .generate_json import create_doctypes_json

def configure_app(app_name, django_path):
    """Register models from multiple modules within an app."""
    
    # # Path to admin.py
    # admin_path = os.path.join(django_path, f"{app_name}_app", 'admin.py')
    # modules = find_modules(app_name)
    
    # # Clear existing content of admin.py and add the admin import
    # with open(admin_path, 'w') as file:
    #     file.write("from django.contrib import admin\n\n")

    # # List to collect import statements and all valid models for registration
    # import_statements = []
    # all_models_to_register = []

    # # Process each module
    # for module in modules:
    #     module_snake_case = to_snake_case(module)
    #     _, module_path = find_module_base_path(app_name=app_name, module_name=module_snake_case)

    #     # Check if the module path exists
    #     if not module_path or not os.path.exists(module_path):
    #         click.echo(f"Module '{module}' does not exist in app '{app_name}'. Skipping...")
    #         continue

    #     # Define paths for 'doc' and 'doctype' folders
    #     doc_path = os.path.join(module_path, module_snake_case, "doc")
    #     doctype_path = os.path.join(module_path, module_snake_case, "doctype")

    #     # Check for 'doc' or 'doctype' folders and process whichever exists
    #     if os.path.isdir(doc_path):
    #         imports, models = process_folder_docs(app_name, module_snake_case, doc_path, django_path)
    #     elif os.path.isdir(doctype_path):
    #         imports, models = process_folder_docs(app_name, module_snake_case, doctype_path, django_path)
    #     else:
    #         click.echo(f"No 'doc' or 'doctype' folder found for module '{module}' in app '{app_name}'.")
    #         continue

    #     # Collect imports and models to register
    #     import_statements.extend(imports)
    #     all_models_to_register.extend(models)

    # # Write collected imports and model registrations to admin.py
    # if import_statements and all_models_to_register:
    #     with open(admin_path, 'a') as file:
    #         # Write import statements
    #         pass
    #         # for statement in import_statements:
    #         #     file.write(statement + "\n")
    #         # file.write("\n")
            
    #         # # Write model registration
    #         # file.write("admin.site.register([\n")
    #         # for model in all_models_to_register:
    #         #     file.write(f"    {model},\n")
    #         # file.write("])\n")

    # Generate the doctypes.json file
    create_doctypes_json(app_name)

def process_folder_docs(app_name, module, folder_path, django_path):
    """Processes each document or doctype in the specified folder and returns model names and import statements."""
    
    import_statements = []
    models_to_register = []

    # Process each item in the folder
    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)

        # Only process directories within the folder
        if os.path.isdir(item_path):
            model_name = underscore_to_titlecase(item_name)
            
            # Register model details
            register_to_model_json(app_name=app_name, module_name=module, doc_name=item_name, django_path=django_path)

            # Generate import statement and add to lists
            import_statement = f"from {app_name}.models.{module}.{item_name} import {model_name}"
            import_statements.append(import_statement)
            models_to_register.append(model_name)
              
    return import_statements, models_to_register

