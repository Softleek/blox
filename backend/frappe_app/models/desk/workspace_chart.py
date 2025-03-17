from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkspaceChart(BaseModel):
    chart_name = models.ForeignKey("frappe_app.DashboardChart", related_name="WorkspaceChartChartName", on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
