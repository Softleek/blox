import re
import os
import ast
from difflib import get_close_matches
import click

def find_matching_class(file_content, model_name):
    """Check if the model_name matches a class in the Python file."""
    parsed_content = ast.parse(file_content)
    class_names = [node.name for node in parsed_content.body if isinstance(node, ast.ClassDef)]
    if model_name in class_names:
        return model_name  # Exact match
    return class_names  # Return all available class names for further matching

def find_nearest_class(model_name, class_names):
    """Find the nearest match to model_name from a list of class names."""
    matches = get_close_matches(model_name, class_names, n=1, cutoff=0.6)
    return matches[0] if matches else None

def write_viewset(view_file, model_name, module_name, folder_path, doc_name):
    """Write a viewset for a given model, skipping the import if the file is missing or empty."""
    model_file_path = os.path.join(folder_path, f"{doc_name}.py")
    
    # Check if the file exists and is not empty
    modelimport_name = None
    if not os.path.exists(model_file_path) or os.path.getsize(model_file_path) == 0:
        pass
    else:

        # Load model file content
        with open(model_file_path, 'r', encoding='utf-8') as f:
            model_data = f.read()
        
        # Skip if the file is empty after reading
        if not model_data.strip():
            return

        # Match the class in the model file
        class_names = find_matching_class(model_data, model_name)
        if isinstance(class_names, list):  # If no exact match, find the nearest
            nearest_class = find_nearest_class(model_name, class_names)
            if not nearest_class:
                raise ValueError(f"No matching or similar class found for {model_name} in {model_file_path}.")
            modelimport_name = nearest_class
        else:
            modelimport_name = model_name


    # Construct import path dynamically
    import_path = '.'.join(re.split(r'[\\/]', os.path.normpath(folder_path))[-5:])
    if modelimport_name:
        view_file.write(f"# from apps.{import_path}.{doc_name} import {modelimport_name} as Custom{model_name}\n\n")
    
    # Write the viewset
    view_file.write(f"class {model_name}ViewSet(GenericViewSet):\n")
    view_file.write(f"    queryset = {model_name}.objects.all()\n")
    view_file.write(f"    filterset_class = {model_name}Filter\n")
    view_file.write(f"    permission_classes = [HasGroupPermission]\n")
    view_file.write(f"    serializer_class = {model_name}Serializer\n\n")
