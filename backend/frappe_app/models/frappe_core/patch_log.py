from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class PatchLog(BaseModel):
    patch = models.CharField(max_length=255, null=True, blank=True)
    skipped = models.BooleanField(default=False, null=True, blank=True)
    traceback = models.CharField(max_length=255, null=True, blank=True)
