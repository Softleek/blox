from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DashboardChartLink(BaseModel):
    chart = models.ForeignKey("frappe_app.DashboardChart", related_name="DashboardChartLinkChart", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_WIDTH = [
        ("Half", "Half"),
        ("Full", "Full"),
    ]
    width = models.CharField(choices=CHOICES_WIDTH, max_length=255, default='Half', null=True, blank=True)
