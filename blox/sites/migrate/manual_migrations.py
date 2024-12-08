import os
import re
import click
from collections import defaultdict

def clear_migration_file(migration_file_path):
    """Clear any existing content in the migration file before writing."""
    with open(migration_file_path, "w") as migration_file:
        migration_file.truncate(0)

def clean_field_params(field_params):
    """Remove 'choices' from field parameters along with everything after it up to the next comma."""
    cleaned_params = re.sub(r"choices\s*=\s*[^,]*,?\s*", "", field_params)
    return cleaned_params.strip().rstrip(",")

def handle_charfield(field_name, field_params):
    cleaned_params = clean_field_params(field_params)
    return f"('{field_name}', models.CharField({cleaned_params}))"

def handle_foreignkey(field_name, field_params, app_name):
    # Clean the field parameters
    cleaned_params = clean_field_params(field_params)

    # Extract the part before the first comma, convert it to lowercase, and reassemble with the rest
    first_comma_index = cleaned_params.find(',')
    if first_comma_index != -1:
        before_comma = cleaned_params[:first_comma_index].lower()
        after_comma = cleaned_params[first_comma_index:]
        cleaned_params = f"{before_comma}{after_comma}"
    else:
        cleaned_params = cleaned_params.lower()

    # Add the `on_delete` parameter if it's not present
    if "on_delete" not in cleaned_params:
        cleaned_params += ", on_delete=models.CASCADE"
    
    # Format the field code with ForeignKey(to= syntax
    return f"('{field_name}', models.ForeignKey({cleaned_params}))".replace("ForeignKey(", "ForeignKey(to=")


def handle_manytomanyfield(field_name, field_params, app_name):
    related_model = re.search(r"'(\w+)'", field_params)
    if related_model:
        related_model_name = related_model.group(1)
        cleaned_params = f"to='{app_name}.{related_model_name}'"
    else:
        cleaned_params = ""
    return f"('{field_name}', models.ManyToManyField({cleaned_params}))"

def create_manual_migrations(app_name, django_path):
    """Create an initial migration file by scanning models in the app's models folder."""
    migrations_folder = os.path.join(django_path, app_name, "migrations")
    models_folder = os.path.join(django_path, app_name, "models")
    migration_file_path = os.path.join(migrations_folder, "0001_initial.py")

    # Ensure the migrations folder exists
    os.makedirs(migrations_folder, exist_ok=True)

    # Clear the migration file before writing
    clear_migration_file(migration_file_path)

    # Dictionary to track dependencies: key is model, value is a set of dependencies
    dependencies = defaultdict(set)
    models_data = {}  # Store model field data to write later

    # Collect all model files in the models folder
    model_files = [os.path.join(root, file) for root, _, files in os.walk(models_folder)
                   for file in files if file.endswith(".py") and not file.startswith("__init__")]

    # Parse each model file
    for model_file in model_files:
        with open(model_file, "r") as file:
            model_content = file.read()

            # Find all model classes in the file
            model_names = re.findall(r"class (\w+)\(BaseModel\):", model_content)
            for model_name in model_names:
                existing_fields = ["id"]
                fields = []
                fields.append("('id', models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True))")

                # Find all fields within the model class
                field_matches = re.findall(r"(\w+)\s*=\s*models\.(\w+)\((.*?)\)", model_content)
                for field_name, field_type, field_params in field_matches:
                    if field_name == 'id':
                        continue
                    existing_fields.append(field_name)
                    # Process each field based on its type
                    if field_type == "CharField":
                        field_code = handle_charfield(field_name, field_params)
                    elif field_type == "ForeignKey":
                        field_code = handle_foreignkey(field_name, field_params, app_name)
                        # Track the model this ForeignKey points to
                        related_model = re.search(r"to='(.+?)\.(.+?)'", field_code)
                        if related_model:
                            dependencies[model_name].add(related_model.group(2))
                    elif field_type == "ManyToManyField":
                        field_code = handle_manytomanyfield(field_name, field_params, app_name)
                        related_model = re.search(r"to='(.+?)\.(.+?)'", field_code)
                        if related_model:
                            dependencies[model_name].add(related_model.group(2))
                    else:
                        # For unsupported field types, use a generic format
                        cleaned_params = clean_field_params(field_params)
                        field_code = f"('{field_name}', models.{field_type}({cleaned_params}))"

                    fields.append(field_code)

                # Add created_at and modified_at if not already in the fields
                if 'created_at' not in existing_fields:
                    fields.append("('created_at', models.DateTimeField(auto_now_add=True))")
                if 'modified_at' not in existing_fields:
                    fields.append("('modified_at', models.DateTimeField(auto_now=True))")

                # Save fields data for each model
                models_data[model_name] = fields

    # Order models based on dependencies
    sorted_models = topological_sort(models_data.keys(), dependencies)

    # Create and write the migration file
    with open(migration_file_path, "w") as migration_file:
        migration_file.write("from django.db import migrations, models\n\n\n")
        migration_file.write("class Migration(migrations.Migration):\n")
        migration_file.write("    initial = True\n\n")
        migration_file.write("    dependencies = []\n\n")
        migration_file.write("    operations = [\n")

        # Write models in dependency order
        for model_name in sorted_models:
            fields = models_data[model_name]
            migration_file.write(f"        migrations.CreateModel(\n")
            migration_file.write(f"            name='{model_name}',\n")
            migration_file.write("            fields=[\n")
            for field_code in fields:
                migration_file.write(f"                {field_code},\n")
            migration_file.write("            ],\n")
            migration_file.write("        ),\n")

        migration_file.write("    ]\n")

    click.echo(f"Manual migration file created at '{migration_file_path}'.")


def topological_sort(models, dependencies):
    """Order models based on dependencies to avoid foreign key conflicts."""
    sorted_models = []
    visited = set()
    temp_stack = set()

    def visit(model):
        if model in visited:
            return
        if model in temp_stack:
            raise ValueError("Circular dependency detected!")
        temp_stack.add(model)
        for dependency in dependencies[model]:
            visit(dependency)
        temp_stack.remove(model)
        visited.add(model)
        sorted_models.append(model)

    for model in models:
        visit(model)

    return sorted_models
