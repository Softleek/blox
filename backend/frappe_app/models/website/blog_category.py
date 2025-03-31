from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class BlogCategory(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    published = models.BooleanField(default=True, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    preview_image = models.CharField(max_length=255, null=True, blank=True)
