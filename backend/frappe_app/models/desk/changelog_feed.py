from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class ChangelogFeed(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    app_name = models.CharField(max_length=255, null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    posting_timestamp = models.DateTimeField(null=True, blank=True)
