from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class MilestoneTracker(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="MilestoneTrackerDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_TRACK_FIELD = [
        ("", ""),
    ]
    track_field = models.CharField(choices=CHOICES_TRACK_FIELD, max_length=255, null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
