from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class DashboardChartField(BaseModel):
    CHOICES_Y_FIELD = [
        ("", ""),
    ]
    y_field = models.CharField(choices=CHOICES_Y_FIELD, max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
