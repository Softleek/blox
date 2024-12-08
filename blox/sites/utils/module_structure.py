import os
from ...utils.config import  find_module_base_path
from ...utils.text import to_snake_case

def get_modules_from_file(custom_app_path,app_name):
    """Retrieve modules from modules.txt, skipping lines that start with '#'.

    Args:
        custom_app_path (str): The path to the app directory.

    Returns:
        list: List of module names found in modules.txt.

    Raises:
        FileNotFoundError: If modules.txt is not found in the specified path.
    """
    # Locate modules.txt and the base path for modules
    modules_file_path, _ = find_module_base_path(app_path=custom_app_path,app_name=app_name)
    
    if not modules_file_path or not os.path.exists(modules_file_path):
        raise FileNotFoundError(f"modules.txt not found in {custom_app_path}")

    # Read and return non-commented module lines from modules.txt
    with open(modules_file_path, 'r') as module_file:
        modules = [
            line.strip() for line in module_file
            if line.strip() and not line.startswith('#')
        ]
    
    return modules


def delete_associated_py_files(folder_path, structure):
    """Delete specific .py files (e.g., views.py, models.py) in the specified folder and its subfolders."""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py') and file.replace('.py', '') in structure:
                os.remove(os.path.join(root, file))



def create_module_structure(app_path, custom_app_path,app_name):
    """Create module directories and sub-files."""
    structure = ['views', 'models', 'tests', 'serializers', 'filters']
    modules = get_modules_from_file(custom_app_path,app_name)
        
    for folder in structure:
        folder_path = os.path.join(app_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        
         # Delete existing .py files in the folder
        delete_associated_py_files(app_path,structure)

        # Initialize __init__.py content
        init_imports = []

        for module in modules:
            module = to_snake_case(module)  # Convert to snake_case
            module_path = os.path.join(folder_path, module)
            os.makedirs(module_path, exist_ok=True)

            # Create individual files for each document in the module's folder
            doc_base_path = os.path.join(custom_app_path, module, 'doc')
            
            if os.path.exists(doc_base_path):
                for subfolder in os.listdir(doc_base_path):
                    subfolder = to_snake_case(subfolder)  # Convert to snake_case
                    subfolder_path = os.path.join(doc_base_path, subfolder)
                    
                    if os.path.isdir(subfolder_path):
                        # Create a .py file for the folder
                        doc_file_path = os.path.join(module_path, f"{subfolder}.py")
                        with open(doc_file_path, 'w') as f:
                            f.write(f"# {subfolder}.py for {folder} in {module} module\n")
                        
                        # Add import statement to init_imports
                        import_statement = f"from .{module}.{subfolder} import *\n"
                        init_imports.append(import_statement)
                    
                    elif subfolder == '__init__.py':
                        # Handle __init__.py if necessary
                        init_file_path = os.path.join(module_path, '__init__.py')
                        with open(init_file_path, 'w') as f:
                            f.write(f"# __init__.py for {folder} in {module} module\n")
        
        # Write import statements to __init__.py
        with open(os.path.join(folder_path, '__init__.py'), 'w') as init_file:
            init_file.write(f"# {folder}\n")
            init_file.writelines(init_imports)