from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class InstalledApplication(BaseModel):
    git_branch = models.CharField(max_length=255, null=True, blank=True)
    app_name = models.CharField(max_length=255, null=True, blank=True)
    app_version = models.CharField(max_length=255, null=True, blank=True)
