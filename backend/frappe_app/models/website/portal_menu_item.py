from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PortalMenuItem(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    enabled = models.BooleanField(default=False, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="PortalMenuItemReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey("frappe_app.Role", related_name="PortalMenuItemRole", on_delete=models.CASCADE, null=True, blank=True)
    target = models.CharField(max_length=255, null=True, blank=True)
