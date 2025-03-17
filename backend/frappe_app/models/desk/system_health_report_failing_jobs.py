from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SystemHealthReportFailingJobs(BaseModel):
    scheduled_job_type = models.ForeignKey("frappe_app.ScheduledJobType", related_name="SystemHealthReportFailingJobsScheduledJobType", on_delete=models.CASCADE, null=True, blank=True)
    failure_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
