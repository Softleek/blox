import os
import click
from .models.reserved_keywords import reserved_keywords
from ...utils.text import to_snake_case

def convert_frappe_fields_to_django(file_content):
    """
    Convert Frappe field types in a class to Django-compatible field definitions.
    """
    field_mappings = {
        "DF.Link": 'models.ForeignKey("{related_model}", on_delete=models.CASCADE, null=True, blank=True)',
        "DF.Currency": "models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)",
        "DF.Date": "models.DateField(null=True, blank=True)",
        "DF.Check": "models.BooleanField(default=False, null=True, blank=True)",
    }

    for frappe_field, django_field in field_mappings.items():
        file_content = file_content.replace(frappe_field, django_field)

    return file_content


@click.command()
@click.option('--folder_path', required=True, help="Path to the Frappe app's folder")
@click.option('--doc_name', required=True, help="Name of the DocType file (without .py extension)")
def convert_frappe_to_django(folder_path, doc_name):
    """
    Convert a Frappe-style Python file to a Django-compatible model file.
    """
    # Define paths for the source and target files
    model_file_path = os.path.join(folder_path, f"{doc_name}.py")
    output_file_path = os.path.join(folder_path, f"{doc_name}_django.py")

    # Check if the source file exists and is non-empty
    if not os.path.exists(model_file_path) or os.path.getsize(model_file_path) == 0:
        click.echo(f"Skipping conversion: File {model_file_path} is missing or empty.")
        return

    # Load the Frappe file content
    with open(model_file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    # Process the file: Convert Frappe fields to Django equivalents
    django_file_content = convert_frappe_fields_to_django(file_content)

    # Write the updated content to the new file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(django_file_content)

    click.echo(f"Django model file created at: {output_file_path}")


if __name__ == "__main__":
    convert_frappe_to_django()
