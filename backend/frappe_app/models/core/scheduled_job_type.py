from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ScheduledJobType(BaseModel):
    method = models.CharField(max_length=255, null=True, blank=True)
    stopped = models.BooleanField(default=False, null=True, blank=True)
    create_log = models.BooleanField(default=False, null=True, blank=True)
    last_execution = models.DateTimeField(null=True, blank=True)
    cron_format = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_FREQUENCY = [
        ("All", "All"),
        ("Hourly", "Hourly"),
        ("Hourly Long", "Hourly Long"),
        ("Daily", "Daily"),
        ("Daily Long", "Daily Long"),
        ("Weekly", "Weekly"),
        ("Weekly Long", "Weekly Long"),
        ("Monthly", "Monthly"),
        ("Monthly Long", "Monthly Long"),
        ("Cron", "Cron"),
        ("Yearly", "Yearly"),
        ("Annual", "Annual"),
    ]
    frequency = models.CharField(choices=CHOICES_FREQUENCY, max_length=255, null=True, blank=True)
    server_script = models.ForeignKey("frappe_app.ServerScript", related_name="ScheduledJobTypeServerScript", on_delete=models.CASCADE, null=True, blank=True)
    next_execution = models.DateTimeField(null=True, blank=True)
    scheduler_event = models.ForeignKey("frappe_app.SchedulerEvent", related_name="ScheduledJobTypeSchedulerEvent", on_delete=models.CASCADE, null=True, blank=True)
