from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class PersonalDataDeletionStep(BaseModel):
    document_type = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Pending", "Pending"),
        ("Deleted", "Deleted"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
    partial = models.BooleanField(default=False, null=True, blank=True)
    fields = models.TextField(null=True, blank=True)
    filtered_by = models.CharField(max_length=255, null=True, blank=True)
