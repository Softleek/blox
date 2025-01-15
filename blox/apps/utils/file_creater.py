import os


def create_files_from_templates(
    base_path, app_name, templates_folder, dynamic_content=None
):
    """Create necessary files for the app by loading content from templates."""

    # Define mapping of template files to their destination paths
    file_mappings = {
        "MANIFEST.in": os.path.join(base_path, "MANIFEST.in"),
        "README.md": os.path.join(base_path, "README.md"),
        "setup.py": os.path.join(base_path, app_name, "setup.py"),
        "hooks.py": os.path.join(base_path, app_name, "hooks.py"),
        "modules.txt": os.path.join(base_path, app_name, "modules.txt"),
        "patches.txt": os.path.join(base_path, app_name, "patches.txt"),
        "__init__.py": os.path.join(base_path, app_name, "__init__.py"),
        # Development and compliance related files
        "tox.ini": os.path.join(base_path, "tox.ini"),
        ".flake8": os.path.join(base_path, ".flake8"),
        ".editorconfig": os.path.join(base_path, ".editorconfig"),
        "requirements-dev.txt": os.path.join(base_path, "requirements-dev.txt"),
        "pyproject.toml": os.path.join(base_path, "pyproject.toml"),
    }

    # Loop through file mappings and create each file with content from the corresponding template
    for template_name, destination_path in file_mappings.items():
        template_path = os.path.join(templates_folder, template_name)

        # Ensure the directory for the destination file exists
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

        # Write the content from the template file to the destination file
        try:
            with open(template_path, "r") as template_file:
                content = template_file.read()

            # Prepend dynamic content if available
            if dynamic_content and template_name in dynamic_content:
                if template_name == "hooks.py":
                    # Insert dynamic content after the second line in hooks.py
                    lines = content.splitlines()
                    # Ensure the file has at least 2 lines to insert content after the second line
                    if len(lines) >= 2:
                        lines.insert(2, dynamic_content[template_name])
                        content = "\n".join(lines)
                    else:
                        content = dynamic_content[template_name] + content
                else:
                    # For other files, prepend the dynamic content
                    content = dynamic_content[template_name] + content

            # Replace placeholders in the template content
            content = content.replace("{{app_name}}", app_name)

            with open(destination_path, "w") as destination_file:
                destination_file.write(content)
        except FileNotFoundError:
            print(
                f"Template file '{template_name}' not found in '{templates_folder}'. Skipping."
            )
        except Exception as e:
            print(f"Error creating file '{destination_path}': {e}")
