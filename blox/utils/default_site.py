import json
import os

import click


def get_default_site_info(PROJECT_ROOT):
    """
    Utility function to get the Django path and site name of the default site.

    :param PROJECT_ROOT: The root directory of the project
    :return: A tuple (django_path, site_name) if a default site is found, otherwise None
    """
    sites_json_path = os.path.join(PROJECT_ROOT, "config", "sites.json")

    if not os.path.exists(sites_json_path):
        click.echo("No sites found in sites.json.")
        return None

    # Load sites from sites.json
    with open(sites_json_path, "r") as json_file:
        sites = json.load(json_file)

    # Find the default site
    selected_site = next((s for s in sites if s.get("default") == True), None)

    if selected_site:
        return selected_site
    else:
        return None
