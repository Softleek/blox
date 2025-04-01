from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class SlackWebhookURL(BaseModel):
    webhook_name = models.CharField(max_length=255, null=True, blank=True)
    webhook_url = models.CharField(max_length=255, null=True, blank=True)
    show_document_link = models.BooleanField(default=True, null=True, blank=True)
