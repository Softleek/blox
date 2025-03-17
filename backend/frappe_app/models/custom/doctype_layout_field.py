from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DocTypeLayoutField(BaseModel):
    CHOICES_FIELDNAME = [
        ("", ""),
    ]
    fieldname = models.CharField(choices=CHOICES_FIELDNAME, max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
