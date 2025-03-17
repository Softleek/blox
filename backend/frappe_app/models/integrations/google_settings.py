from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class GoogleSettings(SingletonModel):
    enable = models.BooleanField(default=False, null=True, blank=True)
    client_id = models.CharField(max_length=255, null=True, blank=True)
    client_secret = models.CharField(max_length=255, null=True, blank=True)
    api_key = models.CharField(max_length=255, null=True, blank=True)
    app_id = models.CharField(max_length=255, null=True, blank=True)
    google_drive_picker_enabled = models.BooleanField(default=False, null=True, blank=True)
