from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Country(BaseModel):
    country_name = models.CharField(max_length=255, null=True, blank=True)
    date_format = models.CharField(max_length=255, null=True, blank=True)
    time_format = models.CharField(max_length=255, default='HH:mm:ss', null=True, blank=True)
    time_zones = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
