from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class UserPermission(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="UserPermissionUser", on_delete=models.CASCADE, null=True, blank=True)
    allow = models.ForeignKey("frappe_app.Doctype", related_name="UserPermissionAllow", on_delete=models.CASCADE, null=True, blank=True)
    for_value = models.CharField(max_length=255, null=True, blank=True)
    is_default = models.BooleanField(default=False, null=True, blank=True)
    apply_to_all_doctypes = models.BooleanField(default=True, null=True, blank=True)
    applicable_for = models.ForeignKey("frappe_app.Doctype", related_name="UserPermissionApplicableFor", on_delete=models.CASCADE, null=True, blank=True)
    hide_descendants = models.BooleanField(default=False, null=True, blank=True)
