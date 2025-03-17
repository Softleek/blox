from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebPageView(BaseModel):
    path = models.CharField(max_length=255, null=True, blank=True)
    referrer = models.CharField(max_length=255, null=True, blank=True)
    browser = models.CharField(max_length=255, null=True, blank=True)
    browser_version = models.CharField(max_length=255, null=True, blank=True)
    is_unique = models.CharField(max_length=255, null=True, blank=True)
    time_zone = models.CharField(max_length=255, null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    visitor_id = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    campaign = models.CharField(max_length=255, null=True, blank=True)
    medium = models.CharField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
