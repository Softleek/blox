from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class UTMSource(BaseModel):
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=255, null=True, blank=True)
