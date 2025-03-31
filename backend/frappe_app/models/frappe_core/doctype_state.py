from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class DocTypeState(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_COLOR = [
        ("Blue", "Blue"),
        ("Cyan", "Cyan"),
        ("Gray", "Gray"),
        ("Green", "Green"),
        ("Light Blue", "Light Blue"),
        ("Orange", "Orange"),
        ("Pink", "Pink"),
        ("Purple", "Purple"),
        ("Red", "Red"),
        ("Yellow", "Yellow"),
    ]
    color = models.CharField(choices=CHOICES_COLOR, max_length=255, default='Blue', null=True, blank=True)
    custom = models.BooleanField(default=False, null=True, blank=True)
