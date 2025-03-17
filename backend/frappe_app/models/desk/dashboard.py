from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Dashboard(BaseModel):
    dashboard_name = models.CharField(max_length=255, null=True, blank=True)
    is_default = models.BooleanField(default=False, null=True, blank=True)
    charts = models.ManyToManyField("frappe_app.DashboardChartLink", related_name="DashboardCharts", )
    chart_options = models.CharField(max_length=255, null=True, blank=True)
    cards = models.ManyToManyField("frappe_app.NumberCardLink", related_name="DashboardCards", )
    is_standard = models.BooleanField(default=False, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="DashboardModule", on_delete=models.CASCADE, null=True, blank=True)
