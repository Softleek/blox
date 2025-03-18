from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class AuditTrail(SingletonModel):
    doctype_name = models.ForeignKey("frappe_app.Doctype", related_name="AuditTrailDoctypeName", on_delete=models.CASCADE, null=True, blank=True)
    document = models.CharField(max_length=255, null=True, blank=True)
    version_table = models.TextField(null=True, blank=True)
    rows_added = models.TextField(null=True, blank=True)
    rows_removed = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
