from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class Salutation(BaseModel):
    salutation = models.CharField(max_length=255, null=True, blank=True)
