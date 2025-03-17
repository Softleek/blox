from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PortalSettings(SingletonModel):
    default_role = models.ForeignKey("frappe_app.Role", related_name="PortalSettingsDefaultRole", on_delete=models.CASCADE, null=True, blank=True)
    hide_standard_menu = models.BooleanField(default=False, null=True, blank=True)
    menu = models.ManyToManyField("frappe_app.PortalMenuItem", related_name="PortalSettingsMenu", )
    custom_menu = models.ManyToManyField("frappe_app.PortalMenuItem", related_name="PortalSettingsCustomMenu", )
    default_portal_home = models.CharField(max_length=255, null=True, blank=True)
