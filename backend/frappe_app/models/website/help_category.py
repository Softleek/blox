from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class HelpCategory(BaseModel):
    category_name = models.CharField(max_length=255, null=True, blank=True)
    category_description = models.TextField(null=True, blank=True)
    published = models.BooleanField(default=False, null=True, blank=True)
    help_articles = models.IntegerField(null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
