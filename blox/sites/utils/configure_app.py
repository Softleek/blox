import os
from ...utils.text import underscore_to_titlecase
from ...utils.register_models import register_to_model_json
from .generate_json import create_doctypes_json

def configure_app(app_name, django_path):
    """Register models from multiple modules within an app."""
    # Generate the doctypes.json file
    create_doctypes_json(app_name)
    
    
def process_folder_docs(app_name, module, folder_path, django_path):
    """Processes each document or doctype in the specified folder and returns model names and import statements."""
    
    import_statements = []
    models_to_register = []

    # Use list comprehension for faster directory listing and processing
    items = [item for item in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, item))]

    for item_name in items:
        model_name = underscore_to_titlecase(item_name)
        
        # Register model details
        register_to_model_json(app_name=app_name, module_name=module, doc_name=item_name, django_path=django_path)

        # Generate import statement and add to lists
        import_statement = f"from {app_name}.models.{module}.{item_name} import {model_name}"
        import_statements.append(import_statement)
        models_to_register.append(model_name)
            
    return import_statements, models_to_register

