from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PermissionLog(BaseModel):
    changed_by = models.ForeignKey("frappe_app.User", related_name="PermissionLogChangedBy", on_delete=models.CASCADE, null=True, blank=True)
    changed_at = models.DateTimeField(null=True, blank=True)
    changes = models.TextField(null=True, blank=True)
    changed_values = models.TextField(null=True, blank=True)
    for_doctype = models.ForeignKey("frappe_app.Doctype", related_name="PermissionLogForDoctype", on_delete=models.CASCADE, null=True, blank=True)
    for_document = models.CharField(max_length=255, null=True, blank=True)
    reference_type = models.ForeignKey("frappe_app.Doctype", related_name="PermissionLogReferenceType", on_delete=models.CASCADE, null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Updated", "Updated"),
        ("Removed", "Removed"),
        ("Added", "Added"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
