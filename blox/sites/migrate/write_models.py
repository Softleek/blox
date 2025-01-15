import os


from .models.json_loader import load_json_file
from .models.model_fields_writer import write_model


def write_model_fields(
    module_file, file_path, folder_path, model_name, doc_name, django_path
):
    """Write model fields based on fields.json or doc_name.json in the given folder path."""
    fields_file_path = os.path.join(folder_path, "fields.json")
    model_file_path = os.path.join(folder_path, f"{doc_name}.json")
    settings_file_path = os.path.join(folder_path, "settings.json")

    field_list = []
    settings = {}

    # Load fields from fields.json or doc_name.json
    if os.path.exists(fields_file_path):
        field_list = load_json_file(fields_file_path)
        # If fields.json exists, load settings.json
        if os.path.exists(settings_file_path):
            settings = load_json_file(settings_file_path)
        else:
            return
    elif os.path.exists(model_file_path):
        # Load data from doc_name.json and extract fields and settings
        model_data = load_json_file(model_file_path)
        field_list = model_data.get("fields", [])
        # Use the rest of the doc_name.json as settings, excluding "fields"
        settings = {k: v for k, v in model_data.items() if k != "fields"}
    else:

        module_file.write("    pass\n\n")
        return

    # If there are no fields, clear the file and write a _ statement
    if not field_list or field_list == [] or field_list is None:

        # Clear the contents of the module file
        module_file.write("    pass\n\n")
        return

    # Write model fields
    write_model(module_file, field_list, model_name, django_path)

    # Write ID field using the settings data
    # write_id_field(module_file, file_path, settings, model_name)
