import os

def create_files(base_path, doc_name):
    """
    Create a doctype folder with Frappe-like files in the given base path.

    Args:
        base_path (str): Path where the doctype folder should be created.
        doc_name (str): Name of the doctype folder.
    """
    # Define the default files and their content
    default_files = {
        f"{doc_name}.py": f"""
# {doc_name.capitalize()} DocType

import frappe
from frappe.model.document import Document

class {doc_name.capitalize()}(Document):
    pass
        """,
        f"{doc_name}.js": f"""
// {doc_name.capitalize()} JavaScript File

frappe.ui.form.on('{doc_name.capitalize()}', {{
    refresh: function (frm) {{
        // Custom script logic here
    }},
}});
        """,
        f"{doc_name}.json": f"""
{{
    "doctype": "{doc_name.capitalize()}",
    "name": "{doc_name.capitalize()}",
    "module": "Module Name",
    "fields": [],
    "permissions": [
        {{
            "role": "System Manager",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1
        }}
    ]
}}
        """,
        f"test_{doc_name}.py": f"""
# Test for {doc_name.capitalize()}

import frappe
import unittest

class Test{doc_name.capitalize()}(unittest.TestCase):
    def test_example(self):
        # Example test case
        self.assertTrue(True)
        """
    }

    # Create the doctype folder
    doc_folder_path = os.path.join(base_path, "doctype", doc_name)
    os.makedirs(doc_folder_path, exist_ok=True)

    # Create the files in the doctype folder
    for filename, content in default_files.items():
        file_path = os.path.join(doc_folder_path, filename)
        with open(file_path, "w") as file:
            file.write(content.strip())  # Remove unnecessary whitespace

    return doc_folder_path  # Return the path for confirmation or further actions
