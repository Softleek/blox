from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class CustomRole(BaseModel):
    page = models.ForeignKey("frappe_app.Page", related_name="CustomRolePage", on_delete=models.CASCADE, null=True, blank=True)
    report = models.ForeignKey("frappe_app.Report", related_name="CustomRoleReport", on_delete=models.CASCADE, null=True, blank=True)
    roles = models.ManyToManyField("frappe_app.HasRole", related_name="CustomRoleRoles", )
    response = models.TextField(null=True, blank=True)
    ref_doctype = models.CharField(max_length=255, null=True, blank=True)
