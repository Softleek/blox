from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class SystemHealthReportQueue(BaseModel):
    queue = models.CharField(max_length=255, null=True, blank=True)
    pending_jobs = models.IntegerField(null=True, blank=True)
