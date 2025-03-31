from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class WebsiteSidebarItem(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    group = models.CharField(max_length=255, null=True, blank=True)
