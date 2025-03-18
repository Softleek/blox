from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DocTypeAction(BaseModel):
    label = models.CharField(max_length=255, null=True, blank=True)
    group = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_ACTION_TYPE = [
        ("Server Action", "Server Action"),
        ("Route", "Route"),
    ]
    action_type = models.CharField(choices=CHOICES_ACTION_TYPE, max_length=255, null=True, blank=True)
    action = models.TextField(null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)
    custom = models.BooleanField(default=False, null=True, blank=True)
