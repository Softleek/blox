from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Translation(BaseModel):
    language = models.ForeignKey("frappe_app.Language", related_name="TranslationLanguage", on_delete=models.CASCADE, null=True, blank=True)
    context = models.CharField(max_length=255, null=True, blank=True)
    contributed = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_CONTRIBUTION_STATUS = [
        ("Pending", "Pending"),
        ("Verified", "Verified"),
        ("Rejected", "Rejected"),
    ]
    contribution_status = models.CharField(choices=CHOICES_CONTRIBUTION_STATUS, max_length=255, null=True, blank=True)
    contribution_docname = models.CharField(max_length=255, null=True, blank=True)
    source_text = models.CharField(max_length=255, null=True, blank=True)
    translated_text = models.CharField(max_length=255, null=True, blank=True)
