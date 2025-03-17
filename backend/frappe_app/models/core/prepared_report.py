from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PreparedReport(BaseModel):
    report_name = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Error", "Error"),
        ("Queued", "Queued"),
        ("Completed", "Completed"),
        ("Started", "Started"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Queued', null=True, blank=True)
    report_end_time = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)
    filters = models.TextField(null=True, blank=True)
    filter_values = models.TextField(null=True, blank=True)
    job_id = models.CharField(max_length=255, null=True, blank=True)
    queued_by = models.CharField(max_length=255, null=True, blank=True)
    queued_at = models.DateTimeField(null=True, blank=True)
    peak_memory_usage = models.IntegerField(null=True, blank=True)
