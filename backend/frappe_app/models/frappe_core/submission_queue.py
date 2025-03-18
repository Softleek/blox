from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SubmissionQueue(BaseModel):
    job_id = models.ForeignKey("frappe_app.RqJob", related_name="SubmissionQueueJobId", on_delete=models.CASCADE, null=True, blank=True)
    ref_doctype = models.ForeignKey("frappe_app.Doctype", related_name="SubmissionQueueRefDoctype", on_delete=models.CASCADE, null=True, blank=True)
    ref_docname = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Queued", "Queued"),
        ("Finished", "Finished"),
        ("Failed", "Failed"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
    enqueued_by = models.CharField(max_length=255, null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
