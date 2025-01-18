import json
import os


from ...utils.config import DOCS_JSON_PATH
from ...utils.file_operations import ensure_file_exists

def load_existing_data():
    """Loads existing data from the JSON file or returns an empty list."""
    ensure_file_exists(DOCS_JSON_PATH, initial_data=[])
    if os.path.exists(DOCS_JSON_PATH):
        try:
            with open(DOCS_JSON_PATH, "r") as json_file:
                content = json_file.read().strip()
                if not content:  # Handle empty file
                    return []
                return json.loads(content)
        except json.JSONDecodeError:
            return []
    return []
