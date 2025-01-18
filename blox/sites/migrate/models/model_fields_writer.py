# from .field_mappings import FIELD_TYPE_MAP
from ....utils.register_models import get_app_module_for_model
from ....utils.text import to_snake_case
from .reserved_keywords import reserved_keywords


def write_model(module_file, fields, model_name, django_path):
    """Main function to generate Django model fields from Frappe fields."""
    field_names = set()  # Set to keep track of field names for duplicate checking

    for field in fields:
        field_id = rename_reserved_keywords(field.get("fieldname", ""))

        # Skip any field that ends with '_id'
        if field_id.endswith("_id") or field_id == "id":
            field_id = f"{field_id}_custom"

        field_type = field.get("fieldtype")

        # Add the field_id to the set of field names
        field_names.add(field_id)

        if field_type == "Select":
            write_choices_field(module_file, field, "models.CharField", max_length=255)
        elif field_type == "Link":
            write_link_field(module_file, field, model_name, django_path)
        elif field_type in ["Table", "MultiSelect", "Table MultiSelect"]:
            write_table_field(module_file, field, model_name, django_path)
        elif field_type in ["Check", "Boolean"]:  # Assuming Check maps to BooleanField
            write_field_declaration(
                module_file,
                field_id,
                "models.BooleanField",
                field_name=field.get("label", ""),
            )
        elif field_type in ["Date"]:
            write_field_declaration(
                module_file,
                field_id,
                "models.DateField",
                field_name=field.get("label", ""),
            )
        elif field_type in ["Datetime"]:
            write_field_declaration(
                module_file,
                field_id,
                "models.DateTimeField",
                field_name=field.get("label", ""),
            )
        elif field_type == "Int":
            write_field_declaration(
                module_file,
                field_id,
                "models.IntegerField",
                field_name=field.get("label", ""),
            )
        elif field_type == "Float":
            write_field_declaration(
                module_file,
                field_id,
                "models.FloatField",
                field_name=field.get("label", ""),
            )
        elif field_type in ["Currency", "Percent"]:
            write_field_declaration(
                module_file,
                field_id,
                "models.DecimalField",
                "max_digits=10, decimal_places=2",
                field_name=field.get("label", ""),
            )
        elif field_type == "Text":
            write_field_declaration(
                module_file,
                field_id,
                "models.TextField",
                field_name=field.get("label", ""),
            )
        elif field_type in [
            "Data"
        ]:  # CharFields for Data and BarcodeField
            write_field_declaration(
                module_file,
                field_id,
                "models.CharField",
                "max_length=255",
                field_name=field.get("label", ""),
            )

        elif field_type == "Duration":
            write_field_declaration(
                module_file,
                field_id,
                "models.DurationField",
                field_name=field.get("label", ""),
            )
        elif field_type in [
            "Small Text",
            "Text Area",
            "Text",
            "Long Text",
            "HTML",
            "HTML Editor",
            "Markdown Editor",
        ]:
            write_field_declaration(
                module_file,
                field_id,
                "models.TextField",
                field_name=field.get("label", ""),
            )
        elif field_type == "Password":
            write_field_declaration(
                module_file,
                field_id,
                "models.CharField",
                "max_length=255",
                field_name=field.get("label", ""),
            )
        elif field_type == "Phone":
            write_field_declaration(
                module_file,
                field_id,
                "models.CharField",
                "max_length=20",
                field_name=field.get("label", ""),
            )
        elif field_type == "Rating":
            write_field_declaration(
                module_file,
                field_id,
                "models.DecimalField",
                "max_digits=2, decimal_places=1",
                field_name=field.get("label", ""),
            )
        elif field_type == "Signature":
            write_field_declaration(
                module_file,
                field_id,
                "models.CharField",
                "max_length=255",
                field_name=field.get("label", ""),
            )
        elif field_type in ["Attach", "Attach Image", "Image", "BarcodeField"]:
            write_field_declaration(
                module_file,
                field_id,
                "models.FileField",
                "upload_to='attachments/'",
                field_name=field.get("label", ""),
            )
        elif field_type == "JSON":
            write_field_declaration(
                module_file,
                field_id,
                "models.JSONField",
                field_name=field.get("label", ""),
            )
        elif field_type == "Time":
            write_field_declaration(
                module_file,
                field_id,
                "models.TimeField",
                field_name=field.get("label", ""),
            )

        elif field_type not in [
            "Section Break",
            "Column Break",
            "Tab Break",
        ]:  # Skip layout fields
            write_field_declaration(
                module_file,
                field_id,
                "models.CharField",
                "max_length=255",
                field_name=field.get("label", ""),
            )


def rename_reserved_keywords(field_id):
    """Rename field ID if it is a reserved keyword."""
    return reserved_keywords.get(field_id, field_id)


def write_field_declaration(
    module_file, field_id, field_type, extra_params="", field_name=""
):
    """Writes a field declaration line in the Django model file with verbose name, null, and blank at the end."""
    module_file.write(f"    {field_id} = {field_type}(")
    if extra_params:
        module_file.write(f"{extra_params}, ")
    if field_type != "models.ManyToManyField":
        module_file.write("null=True, blank=True")
    module_file.write(")\n")


def write_choices_field(module_file, field, field_type, max_length=None):
    """Handles Select and MultiSelect fields with choices."""
    field_id = rename_reserved_keywords(field.get("fieldname", ""))
    choices = field.get("options", "").strip().split("\n")

    if choices:
        options_var = f"CHOICES_{field_id.upper()}"
        module_file.write(f"    {options_var} = [\n")
        for choice in choices:
            sanitized_choice = choice.replace(
                '"', "'"
            )  # Replace internal double quotes with single quotes
            module_file.write(
                f'        ("{sanitized_choice}", "{sanitized_choice}"),\n'
            )  # Use double quotes outside
        module_file.write("    ]\n")

        # Set max_length if provided
        max_length_param = f", max_length={max_length}" if max_length else ""
        write_field_declaration(
            module_file,
            field_id,
            field_type,
            f"choices={options_var}{max_length_param}",
            field.get("label", ""),
        )


def write_link_field(module_file, field, model_name, django_path):
    """Handles Link fields (ForeignKey relations)."""
    field_id = rename_reserved_keywords(field.get("fieldname", ""))
    related_model = field.get("options", "'self'")

    app_name, _ = get_app_module_for_model(to_snake_case(related_model), django_path)
    # Ensure related_model is formatted correctly
    related_model = "".join(
        part.capitalize() for part in related_model.replace("_", " ").split()
    )
    modela_name = "".join(
        part.capitalize() for part in field_id.replace("_", " ").split()
    )

    # Create a related_name based on the field's label and the model's name
    related_name = f"{model_name}{modela_name}"
    if app_name:
        related_model = f"{app_name}_app.{related_model}"
    else:
        pass
    write_field_declaration(
        module_file,
        field_id,
        "models.ForeignKey",
        f'"{related_model}", related_name="{related_name}", on_delete=models.CASCADE',
        field_name=field.get("label", ""),
    )


def write_table_field(module_file, field, model_name, django_path):
    """Handles Link fields (ForeignKey relations)."""
    field_id = rename_reserved_keywords(field.get("fieldname", ""))
    related_model = field.get("options", "'self'")

    app_name, _ = get_app_module_for_model(to_snake_case(related_model), django_path)
    # Ensure related_model is formatted correctly
    related_model = "".join(
        part.capitalize() for part in related_model.replace("_", " ").split()
    )
    modela_name = "".join(
        part.capitalize() for part in field_id.replace("_", " ").split()
    )

    # Create a related_name based on the field's label and the model's name
    related_name = f"{model_name}{modela_name}"
    if app_name:
        related_model = f"{app_name}_app.{related_model}"
    else:
        pass

    write_field_declaration(
        module_file,
        field_id,
        "models.ManyToManyField",
        f'"{related_model}", related_name="{related_name}"',
        field_name=field.get("label", ""),
    )


def write_save_method(module_file, fields):
    """Writes the save method to handle barcode generation and other custom logic."""
    module_file.write("\n    def save(self, *args, **kwargs):\n")
    for field in fields:
        if field.get("fieldtype") == "BarcodeField":
            field_id = rename_reserved_keywords(field.get("fieldname", ""))
            module_file.write(
                f"        if not self.{field_id} or not os.path.exists(os.path.join(settings.MEDIA_ROOT, self.{field_id}.name)):\n"
            )
            module_file.write(
                f"            self = write_barcode(self, self.{field_id})\n"
            )
    module_file.write("        super().save(*args, **kwargs)\n\n")
