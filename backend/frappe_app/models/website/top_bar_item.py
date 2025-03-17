from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class TopBarItem(BaseModel):
    label = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_PARENT_LABEL = [
        ("", ""),
    ]
    parent_label = models.CharField(choices=CHOICES_PARENT_LABEL, max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    right = models.BooleanField(default=True, null=True, blank=True)
    open_in_new_tab = models.BooleanField(default=False, null=True, blank=True)
