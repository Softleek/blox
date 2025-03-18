from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PermissionInspector(SingletonModel):
    ref_doctype = models.ForeignKey("frappe_app.Doctype", related_name="PermissionInspectorRefDoctype", on_delete=models.CASCADE, null=True, blank=True)
    docname = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="PermissionInspectorUser", on_delete=models.CASCADE, null=True, blank=True)
    output = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_PERMISSION_TYPE = [
        ("read", "read"),
        ("write", "write"),
        ("create", "create"),
        ("delete", "delete"),
        ("submit", "submit"),
        ("cancel", "cancel"),
        ("select", "select"),
        ("amend", "amend"),
        ("print", "print"),
        ("email", "email"),
        ("report", "report"),
        ("import", "import"),
        ("export", "export"),
        ("share", "share"),
    ]
    permission_type = models.CharField(choices=CHOICES_PERMISSION_TYPE, max_length=255, null=True, blank=True)
