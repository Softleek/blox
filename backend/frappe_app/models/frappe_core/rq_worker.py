from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class RQWorker(BaseModel):
    worker_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    current_job_id = models.ForeignKey("frappe_app.RqJob", related_name="RQWorkerCurrentJobId", on_delete=models.CASCADE, null=True, blank=True)
    pid = models.CharField(max_length=255, null=True, blank=True)
    last_heartbeat = models.DateTimeField(null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    successful_job_count = models.IntegerField(null=True, blank=True)
    failed_job_count = models.IntegerField(null=True, blank=True)
    total_working_time = models.DurationField(null=True, blank=True)
    queue = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_QUEUE_TYPE = [
        ("default", "default"),
        ("long", "long"),
        ("short", "short"),
    ]
    queue_type = models.CharField(choices=CHOICES_QUEUE_TYPE, max_length=255, null=True, blank=True)
    utilization_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
