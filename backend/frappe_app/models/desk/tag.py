from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Tag(BaseModel):
    description = models.TextField(null=True, blank=True)
