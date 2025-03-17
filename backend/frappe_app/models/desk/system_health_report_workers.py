from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SystemHealthReportWorkers(BaseModel):
    queues = models.CharField(max_length=255, null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    utilization = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    failed_jobs = models.IntegerField(null=True, blank=True)
