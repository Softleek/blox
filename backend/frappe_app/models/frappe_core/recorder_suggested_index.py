from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class RecorderSuggestedIndex(BaseModel):
    table = models.CharField(max_length=255, null=True, blank=True)
    column = models.CharField(max_length=255, null=True, blank=True)
