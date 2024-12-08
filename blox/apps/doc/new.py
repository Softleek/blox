import os
import shutil
import click
from ...utils.config import PROJECT_ROOT

@click.command()
@click.argument("doc_name")
@click.option("--app", type=str, help="Select the app by number or name.")
@click.option("--module", type=str, help="Select the module by number or name.")
def newdoc(doc_name, app, module):
    """Create a new documentation folder with default files in the specified module."""

    # Load available apps
    apps_txt_path = os.path.join(PROJECT_ROOT, "config", "apps.txt")
    apps = []
    with open(apps_txt_path, "r") as f:
        apps = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not apps:
        click.echo("No apps found.")
        return

    # Determine app selection
    if app is None:
        click.echo("Select an app:")
        for i, app_name in enumerate(apps):
            click.echo(f"{i + 1}: {app_name}")
        app_choice = click.prompt("Enter the number of the app or the app name", type=str)
        if app_choice.isdigit():
            app_index = int(app_choice) - 1
            selected_app = apps[app_index] if 0 <= app_index < len(apps) else None
        else:
            selected_app = app_choice if app_choice in apps else None
    else:
        selected_app = app if app in apps else None

    if selected_app is None:
        click.echo("Invalid app selection.")
        return

    # Load available modules for the selected app
    module_txt_path = os.path.join(PROJECT_ROOT, "apps", selected_app, "modules.txt")
    modules = []
    with open(module_txt_path, "r") as f:
        modules = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not modules:
        click.echo(f"No modules found for app '{selected_app}'.")
        return

    # Determine module selection
    if module is None:
        click.echo("Select a module:")
        for i, module_name in enumerate(modules):
            click.echo(f"{i + 1}: {module_name}")
        module_choice = click.prompt("Enter the number of the module or the module name", type=str)
        if module_choice.isdigit():
            module_index = int(module_choice) - 1
            selected_module = modules[module_index] if 0 <= module_index < len(modules) else None
        else:
            selected_module = module_choice if module_choice in modules else None
    else:
        selected_module = module if module in modules else None

    if selected_module is None:
        click.echo("Invalid module selection.")
        return

    # Define paths
    module_path = os.path.join(PROJECT_ROOT, "apps", selected_app, selected_module)
    doc_folder_path = os.path.join(module_path, "doc", doc_name)

    # Create the new documentation folder
    os.makedirs(doc_folder_path, exist_ok=True)

    # Define the default files to create
    default_files = {
        "detail.js": """
// // CustomHeader component
// export const CustomHeader = () => {
//   return <></>;
// };

// // CustomBody component
// export const CustomBody = ({ data }) => {
//   return <></>;
// };

// // CustomFooter component
// export const CustomFooter = () => {
//   return <></>;
// };

// // AppendBeforeBody component
// export const AppendBeforeBody = ({ data }) => {
//   return <></>;
// };

// // AppendAfterBody component
// export const AppendAfterBody = () => {
//   return <></>;
// };

// export const header = true;
// export const footer = true;
// export const body = true;
        """,
        "fields.js": "",
        "fields.json": "{}",
        "list.js": """
// // CustomPagination component
// export const CustomPagination = () => {
//   return <></>;
// };

// // CustomFilters component
// export const CustomFilters = () => {
//   return <></>;
// };

// // CustomTable component
// export const CustomTable = () => {
//   return <></>;
// };
// // AppendBeforeBody component
// export const AppendBeforeBody = () => {
//   return <></>;
// };

// // AppendAfterBody component
// export const AppendAfterBody = () => {
//   return <></>;
// };
        """,
        "settings.json": "{}",
        "views.py": ""
    }

    # Create each file with the specified content
    for filename, content in default_files.items():
        file_path = os.path.join(doc_folder_path, filename)
        with open(file_path, "w") as file:
            file.write(content)

    click.echo(f"The documentation folder '{doc_name}' has been created successfully in '{selected_module}'.")
