from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class WebhookHeader(BaseModel):
    key = models.TextField(null=True, blank=True)
    value = models.TextField(null=True, blank=True)
