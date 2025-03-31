from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class SchedulerEvent(BaseModel):
    scheduled_against = models.ForeignKey("frappe_app.Doctype", related_name="SchedulerEventScheduledAgainst", on_delete=models.CASCADE, null=True, blank=True)
    method = models.CharField(max_length=255, null=True, blank=True)
