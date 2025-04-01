from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class DashboardChartSource(BaseModel):
    source_name = models.CharField(max_length=255, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="DashboardChartSourceModule", on_delete=models.CASCADE, null=True, blank=True)
    timeseries = models.BooleanField(default=False, null=True, blank=True)
