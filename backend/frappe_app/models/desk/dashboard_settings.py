from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DashboardSettings(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="DashboardSettingsUser", on_delete=models.CASCADE, null=True, blank=True)
    chart_config = models.CharField(max_length=255, null=True, blank=True)
