from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class GeolocationSettings(SingletonModel):
    CHOICES_PROVIDER = [
        ("Geoapify", "Geoapify"),
        ("Nomatim", "Nomatim"),
        ("HERE", "HERE"),
    ]
    provider = models.CharField(choices=CHOICES_PROVIDER, max_length=255, null=True, blank=True)
    api_key = models.CharField(max_length=255, null=True, blank=True)
    enable_address_autocompletion = models.BooleanField(default=False, null=True, blank=True)
    base_url = models.CharField(max_length=255, null=True, blank=True)
