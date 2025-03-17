from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NavbarSettings(SingletonModel):
    app_logo = models.CharField(max_length=255, null=True, blank=True)
    settings_dropdown = models.ManyToManyField("frappe_app.NavbarItem", related_name="NavbarSettingsSettingsDropdown", )
    help_dropdown = models.ManyToManyField("frappe_app.NavbarItem", related_name="NavbarSettingsHelpDropdown", )
    announcement_widget = models.CharField(max_length=255, null=True, blank=True)
