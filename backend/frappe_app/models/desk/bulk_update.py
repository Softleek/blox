from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class BulkUpdate(SingletonModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="BulkUpdateDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_FIELD = [
        ("", ""),
    ]
    field = models.CharField(choices=CHOICES_FIELD, max_length=255, null=True, blank=True)
    update_value = models.TextField(null=True, blank=True)
    condition = models.TextField(null=True, blank=True)
    limit = models.IntegerField(default=500, null=True, blank=True)
