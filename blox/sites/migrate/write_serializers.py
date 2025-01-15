import os
import re


from ...utils.text import to_snake_case, to_titlecase_no_space
from .models.field_mappings import get_field_type
from .models.json_loader import load_json_file
from .models.reserved_keywords import reserved_keywords


def rename_reserved_keywords(field_id):
    """
    Rename field ID if it is a reserved keyword.
    """
    return reserved_keywords.get(field_id, field_id)


def sanitize_field_name(field_id):
    """
    Sanitize the field name to ensure it is a valid Python variable name.
    - Replace invalid characters with underscores.
    - Prefix with an underscore if the name starts with a digit.
    """
    sanitized = re.sub(r"\W|^(?=\d)", "_", field_id)
    return sanitized


def load_fields(folder_path, doc_name):
    """
    Load fields from doc_name.json.
    """
    model_file_path = os.path.join(folder_path, f"{doc_name}.json")

    field_list = []

    if os.path.exists(model_file_path):
        model_data = load_json_file(model_file_path)
        field_list = model_data.get("fields", [])
    else:
        return []

    return field_list


def write_serializers_header(
    module_file, app_name, module_name, model_name, doc_name, related_fields
):
    """
    Write the imports for the serializers at the top of the file.
    Only import serializers for related models that are not the same as the current model.
    """
    # Start with basic imports
    module_file.write(
        f"from rest_framework import serializers\n"
        f"from core.serializers.template import RelationshipHandlerMixin\n"
    )

    # Import the main model for the current serializer
    module_file.write(
        f"from {app_name}.models.{module_name}.{doc_name} import {model_name}\n\n"
    )

    # # Import serializers for related models only if they are different from the current model
    # for field_name, related_info in related_fields.items():
    #     if not related_info:
    #         continue  # Skip if related_info is empty or None

    #     # Ensure 'model' exists in related_info dictionary
    #     related_model = related_info.get('model', None)

    #     if related_model is None:
    #         continue  # Skip if the 'model' key is not found in related_info

    #     if related_model == model_name:  # Skip if the related model is the same as the current model
    #         continue  # Do not import the serializer for the current model itself

    #     # Fetch the details for the related model
    #     appur_name, modulur_name, related_file = get_doc_details(related_model)

    #     # Create the related serializer's name
    #     serializer_name = f"{to_titlecase_no_space(related_model)}"

    #     # Write the import statement for the related serializer
    #     module_file.write(
    #         # f"def get_{to_snake_case(serializer_name)}():\n"
    #         f"from {appur_name}_app.models.{modulur_name}.{related_file} import {serializer_name}\n"
    #         # f"        return {serializer_name}\n\n"
    #     )


def write_meta_class(module_file, model_name, related_fields):
    """
    Write the Meta class, including related fields, for the serializer.
    """
    module_file.write("    class Meta:\n")
    module_file.write(f"        model = {model_name}\n")
    module_file.write("        fields = '__all__'\n")
    # if related_fields:
    #     module_file.write("        related_fields: Dict[str, Dict[str, str]] = {\n")
    #     for field_name, related_info in related_fields.items():
    #         if related_info.get("self_referencing"):
    #             continue
    #         model_field = related_info["model"]
    #         many = related_info["many"]
    #         serializer_class_name = related_info["serializer"]
    #         module_file.write(
    #             f"            '{field_name}': {{'model': {to_titlecase_no_space(model_field)}, 'many': {str(many).title()}}},\n"
    #         )
    #     module_file.write("        }\n\n")


def process_field(field, model_name, current_doc_name):
    """
    Process a single field and return its related field definition if applicable.
    Handles nested representation for self-referencing fields, ManyToManyField, and OneToOneField relationships.
    """
    if not isinstance(field, dict):
        raise ValueError(f"Invalid field format: {field}. Expected a dictionary.")

    # Rename and sanitize the field name
    raw_field_id = field.get("fieldname", "")
    field_id = sanitize_field_name(
        rename_reserved_keywords(to_snake_case(raw_field_id).lower())
    )
    field_type = get_field_type(field.get("fieldtype", ""))
    related_fields = {}

    # Skip fields ending with '_id' or named 'id'
    if field_id.endswith("_id") or field_id == "id":
        return related_fields

    if field_type in ["Link", "ForeignKey", "ManyToManyField", "OneToOneField"]:
        related_model = field.get("options", "")
        if not related_model:
            raise ValueError(
                f"Field {field_id} has a '{field_type}' type but no related model specified."
            )

        # Check if the related model is the same as the current serializer's model
        # if to_snake_case(related_model) == current_doc_name:
        #     return {field_id: {"self_referencing": True}}

        # Determine the serializer name for the related model
        serializer_name = f"{to_titlecase_no_space(related_model)}Serializer"
        related_fields[field_id] = {
            "model": related_model,
            "serializer": serializer_name,
            "many": False,  # Default for relationships
        }

        # Update the 'many' property for ManyToManyField relationships
        if field_type == "ManyToManyField":
            related_fields[field_id]["many"] = True

        # Add special handling for OneToOneField relationships
        if field_type == "OneToOneField":
            related_fields[field_id]["one_to_one"] = True

    return related_fields


def write_serializer(
    module_file, app_name, module_name, model_name, doc_name, doc_folder_path
):
    """
    Generate and write a single serializer class for the given model, focusing on related fields.
    Use SerializerMethodField for self-referencing fields and declare related fields before Meta.
    """
    fields = load_fields(doc_folder_path, doc_name)

    related_fields = {}
    # for field in fields:
    #     field_related = process_field(field, model_name, doc_name)
    #     related_fields.update(field_related)

    # Write imports
    write_serializers_header(
        module_file, app_name, module_name, model_name, doc_name, related_fields
    )

    # Start defining the main serializer class
    module_file.write(
        f"class {model_name}Serializer(RelationshipHandlerMixin, serializers.ModelSerializer):\n\n"
    )

    # # Declare related fields before Meta
    # for field_name, related_info in related_fields.items():
    #     related_model = related_info.get('model', None)
    #     appur_name, modulur_name, related_file = get_doc_details(related_model)
    #     if related_info.get("self_referencing"):
    #         # Use SerializerMethodField for self-referencing fields
    #         module_file.write(f"    {field_name} = serializers.SerializerMethodField()\n")
    #     else:
    #         # Use the related serializer for other related fields
    #         serializer_class = related_info["serializer"]
    #         many = related_info["many"]
    #         serializer_name = f"{to_titlecase_no_space(related_model)}"

    #         module_file.write(
    #             f"    {field_name} = serializers.PrimaryKeyRelatedField(queryset={serializer_name}.objects.all())\n"
    #         )
    # module_file.write("\n")

    # # Define SerializerMethodField methods for self-referencing fields
    # for field_name, related_info in related_fields.items():
    #     if related_info.get("self_referencing"):
    #         module_file.write(
    #             f"    def get_{field_name}(self, obj):\n"
    #             f"        related_items = obj.{field_name}.all() if hasattr(obj, '{field_name}') else []\n"
    #             f"        return {model_name}Serializer(related_items, many=True).data\n\n"
    #         )

    # Write the Meta class for the serializer
    write_meta_class(module_file, model_name, related_fields)

    # for field_name, related_info in related_fields.items():
    #     if not related_info:
    #         continue  # Skip if related_info is empty or None

    #     # Ensure 'model' exists in related_info dictionary
    #     related_model = related_info.get('model', None)

    #     if related_model is None:
    #         continue  # Skip if the 'model' key is not found in related_info

    #     if related_model == model_name:  # Skip if the related model is the same as the current model
    #         continue  # Do not import the serializer for the current model itself

    #     # Fetch the details for the related model
    #     appur_name, modulur_name, related_file = get_doc_details(related_model)

    #     # Create the related serializer's name
    #     serializer_name = f"{to_titlecase_no_space(related_model)}"

    #     # Write the import statement for the related serializer
    #     module_file.write(
    #        f"    def get_{field_name}(self, obj):\n"
    #         f"        from {appur_name}_app.models.{modulur_name}.{related_file} import {serializer_name}\n"
    #         f"        try:\n"
    #         f"            return {serializer_name}(obj.{field_name}).data\n"
    #         f"        except: return None\n\n"
    #     )
