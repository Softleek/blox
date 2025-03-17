from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ScheduledJobLog(BaseModel):
    CHOICES_STATUS = [
        ("Scheduled", "Scheduled"),
        ("Complete", "Complete"),
        ("Failed", "Failed"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)
    scheduled_job_type = models.ForeignKey("frappe_app.ScheduledJobType", related_name="ScheduledJobLogScheduledJobType", on_delete=models.CASCADE, null=True, blank=True)
    debug_log = models.CharField(max_length=255, null=True, blank=True)
