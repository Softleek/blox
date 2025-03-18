from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class RQJob(BaseModel):
    CHOICES_QUEUE = [
        ("default", "default"),
        ("short", "short"),
        ("long", "long"),
    ]
    queue = models.CharField(choices=CHOICES_QUEUE, max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("queued", "queued"),
        ("started", "started"),
        ("finished", "finished"),
        ("failed", "failed"),
        ("deferred", "deferred"),
        ("scheduled", "scheduled"),
        ("canceled", "canceled"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
    job_id = models.CharField(max_length=255, null=True, blank=True)
    exc_info = models.CharField(max_length=255, null=True, blank=True)
    job_name = models.CharField(max_length=255, null=True, blank=True)
    arguments = models.CharField(max_length=255, null=True, blank=True)
    timeout = models.DurationField(null=True, blank=True)
    time_taken = models.DurationField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
