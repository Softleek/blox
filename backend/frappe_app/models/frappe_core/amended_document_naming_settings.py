from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class AmendedDocumentNamingSettings(BaseModel):
    CHOICES_ACTION = [
        ("Amend Counter", "Amend Counter"),
        ("Default Naming", "Default Naming"),
    ]
    action = models.CharField(choices=CHOICES_ACTION, max_length=255, default='Amend Counter', null=True, blank=True)
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="AmendedDocumentNamingSettingsDocumentType", on_delete=models.CASCADE, null=True, blank=True)
