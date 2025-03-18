from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ModuleDef(BaseModel):
    module_name = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_APP_NAME = [
        ("", ""),
    ]
    app_name = models.CharField(choices=CHOICES_APP_NAME, max_length=255, null=True, blank=True)
    restrict_to_domain = models.ForeignKey("frappe_app.Domain", related_name="ModuleDefRestrictToDomain", on_delete=models.CASCADE, null=True, blank=True)
    custom = models.BooleanField(default=False, null=True, blank=True)
    package = models.ForeignKey("frappe_app.Package", related_name="ModuleDefPackage", on_delete=models.CASCADE, null=True, blank=True)
