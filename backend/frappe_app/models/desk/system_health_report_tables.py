from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SystemHealthReportTables(BaseModel):
    table = models.CharField(max_length=255, null=True, blank=True)
    size = models.FloatField(null=True, blank=True)
