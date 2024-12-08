import os
import click
import re
from ...utils.config import APPS_PATH, find_module_base_path 
from ..utils.generate_json import add_single_entry
from ...utils.text import to_snake_case, to_titlecase_no_space
from .write_models import write_model_fields
from .write_filters import write_filters
from .write_serializers import write_serializer
from .write_viewsets import write_viewset
from .models.json_loader import load_json_file
from ..utils.app_actions import get_name_by_id

STRUCTURE = {
    "views": "views",
    "models": "models",
    "filters": "filters",
    "serializers": "serializers",
    "tests": "tests",
}


def migrate_doc(app_name, module, doc=None, doctype=None, django_path=""):
    """Migrate a specific document within a module and app."""

    module_name = to_snake_case(module).lower()
    doc_name = to_snake_case(doc).lower() if doc else (to_snake_case(doctype).lower() if doctype else None)
    doctype_folder_name = "doc" if doc else "doctype"

    modules_file_path, module_base_path = find_module_base_path(app_name=app_name, module_name=module_name)
    if not module_base_path:
        return  # Exit if no valid path is found

    doc_folder_path = os.path.join(module_base_path, module_name, doctype_folder_name, doc_name)
   
    for folder, structure_name in STRUCTURE.items():
        module_file_path = os.path.join(django_path, f"{app_name}_app", folder, module_name if doc_name else "")
        document_file_path = os.path.join(module_file_path, f"{doc_name}.py" if doc_name else "")

        if not doc_name:
            continue

        ensure_directory(module_file_path)
        ensure_init_file(module_file_path, doc_name)
        
        if os.path.exists(doc_folder_path) and os.path.isdir(doc_folder_path)  and not doc_folder_path.startswith(("_", "pycache")):
            write_module_content(folder, document_file_path,  f"{app_name}_app", module_name, doc_name, doc_folder_path,django_path)

def ensure_directory(path):
    """Ensure the directory exists."""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def ensure_init_file(module_file_path, doc_name):
    """Ensure an __init__.py file exists in the module directory and imports the document."""
    init_file_path = os.path.join(module_file_path, "__init__.py")
    if not os.path.exists(init_file_path):
        with open(init_file_path, "w") as init_file:
            init_file.write("")
    
    import_statement = f"from .{doc_name} import *\n"
    with open(init_file_path, "r+") as init_file:
        lines = init_file.readlines()
        if import_statement not in lines:
            init_file.write(import_statement)

def write_module_content(folder, module_file_path, app_name, module_name, doc_name, doc_folder_path,django_path):
    """Write appropriate content to the module file based on the folder type."""
    model_name = to_titlecase_no_space(get_name_by_id(doc_name, "doc"))
    
    with open(module_file_path, "w+") as module_file:
        if folder == "models":
            write_model_header(module_file, model_name)
            write_model_fields(module_file, module_file_path, doc_folder_path, model_name,doc_name,django_path)
        elif folder == "views":
            write_views_header(module_file, app_name, module_name, model_name, doc_name)
            write_viewset(module_file, model_name, module_name, doc_folder_path, doc_name)
        elif folder == "serializers":
         write_serializer(module_file, app_name, module_name, model_name, doc_name, doc_folder_path)
        elif folder == "filters":
           write_filters(module_file, app_name, module_name, model_name, doc_name, doc_folder_path)
            
def write_model_header(module_file, model_name):
    """Write the imports and class definition header for models."""
    module_file.write(
        "from django.db import models\nfrom core.models import *\n"
        "from multiselectfield import MultiSelectField\n"
        "from core.models.template import BaseModel\n"
        "import uuid\nimport os\nfrom django.conf import settings\n\n"
    )
    module_file.write(f"class {model_name}(BaseModel):\n")
    

def write_views_header(module_file, app_name, module_name, model_name, doc_name):
    """Write the imports and class definition header for views."""
    module_file.write(
        f"from rest_framework import viewsets\n"
        f"from core.views.template import GenericViewSet\n"
        f"from {app_name}.models.{module_name}.{doc_name} import {model_name}\n"
        f"from {app_name}.filters.{module_name}.{doc_name} import {model_name}Filter\n"
        f"from {app_name}.serializers.{module_name}.{doc_name} import {model_name}Serializer\n"
        f"from core.permissions import HasGroupPermission\n\n"
    )

