from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class PrintStyle(BaseModel):
    print_style_name = models.CharField(max_length=255, null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    standard = models.BooleanField(default=False, null=True, blank=True)
    css = models.CharField(max_length=255, null=True, blank=True)
    preview = models.CharField(max_length=255, null=True, blank=True)
