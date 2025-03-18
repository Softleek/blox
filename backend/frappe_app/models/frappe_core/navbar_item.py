from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NavbarItem(BaseModel):
    item_label = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_ITEM_TYPE = [
        ("Route", "Route"),
        ("Action", "Action"),
        ("Separator", "Separator"),
    ]
    item_type = models.CharField(choices=CHOICES_ITEM_TYPE, max_length=255, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)
    is_standard = models.BooleanField(default=False, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    action = models.CharField(max_length=255, null=True, blank=True)
    condition = models.CharField(max_length=255, null=True, blank=True)
