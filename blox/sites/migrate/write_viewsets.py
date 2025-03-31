import ast
import os
import re
from difflib import get_close_matches
from typing import List, Optional, Union, Dict, Any
from .models.json_loader import load_json_file
from ...utils.config import DJANGO_PATH


def find_matching_class(file_content: str, model_name: str) -> Union[str, List[str]]:
    """
    Check if the model_name matches a class in the Python file.
    Returns either the exact match or all available class names.
    """
    parsed_content = ast.parse(file_content)
    class_names = [
        node.name for node in parsed_content.body if isinstance(node, ast.ClassDef)
    ]
    return model_name if model_name in class_names else class_names


def find_nearest_class(model_name: str, class_names: List[str]) -> Optional[str]:
    """
    Find the nearest match to model_name from a list of class names.
    Returns the best match or None if no good match found.
    """
    matches = get_close_matches(model_name, class_names, n=1, cutoff=0.6)
    return matches[0] if matches else None


def write_viewset(
    view_file, 
    model_name: str, 
    module_name: str, 
    folder_path: str, 
    doc_name: str
) -> None:
    """
    Write a viewset for a given model, selecting between GenericViewSet and
    SingleInstanceViewSet based on the issingle flag in the config.
    """
    config_file_path = os.path.join(folder_path, f"{doc_name}.json")
    config = load_json_file(config_file_path) if os.path.exists(config_file_path) else {}
    
    is_single = str(config.get("issingle", "")).lower() in ("1", "true")
    viewset_class = "SingleInstanceViewSet" if is_single else "GenericViewSet"
    
    # Write the main viewset
    view_file.write(f"class {model_name}ViewSet({viewset_class}):\n")
    view_file.write(f"    queryset = {model_name}.objects.all()\n")
    
    if not is_single:
        view_file.write(f"    filterset_class = {model_name}Filter\n")
    
    view_file.write(f"    permission_classes = [HasGroupPermission]\n")
    view_file.write(f"    serializer_class = {model_name}Serializer\n\n")
    view_file.write(f"    filterset_class = {model_name}Filter\n")

    # Add public viewset if configured
    if config.get("is_public", False):
        public_viewset_class = "SingleInstanceViewSet" if is_single else "GenericViewSet"
        view_file.write(f"class Public{model_name}ViewSet({public_viewset_class}):\n")
        view_file.write(f"    queryset = {model_name}.objects.all()\n")
        view_file.write(f"    serializer_class = {model_name}Serializer\n")
        view_file.write(f"    filterset_class = {model_name}Filter\n")
        view_file.write(f"    permission_classes = [AllowAny]\n")
        view_file.write(f"    http_method_names = ['get']\n\n")


def add_import_to_signals(app_name: str, module_name: str, doc_name: str) -> None:
    """
    Add import statement to signals.py if not already present.
    """
    signals_path = os.path.join(DJANGO_PATH, f"{app_name}_app", "signals.py")
    import_statement = f"from {app_name}.{module_name}.doctype.{doc_name}.{doc_name} import *"
    
    if not os.path.exists(signals_path):
        with open(signals_path, "w") as f:
            f.write(f"{import_statement}\n")
        return

    with open(signals_path, "r") as f:
        if import_statement not in f.read():
            with open(signals_path, "a") as f:
                f.write(f"\n{import_statement}")


def clear_signals(app_name: str) -> None:
    """
    Clear all content from signals.py file.
    """
    signals_path = os.path.join(DJANGO_PATH, f"{app_name}_app", "signals.py")
    try:
        if os.path.exists(signals_path):
            with open(signals_path, "w"):
                pass  # Simply opening in write mode clears the file
    except Exception as e:
        print(f"Error clearing signals for {app_name}: {e}")