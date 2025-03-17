from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ClientScript(BaseModel):
    dt = models.ForeignKey("frappe_app.Doctype", related_name="ClientScriptDt", on_delete=models.CASCADE, null=True, blank=True)
    script = models.CharField(max_length=255, null=True, blank=True)
    sample = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_VIEW = [
        ("List", "List"),
        ("Form", "Form"),
    ]
    view = models.CharField(choices=CHOICES_VIEW, max_length=255, default='Form', null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="ClientScriptModule", on_delete=models.CASCADE, null=True, blank=True)
