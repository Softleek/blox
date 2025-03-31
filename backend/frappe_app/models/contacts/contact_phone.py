from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class ContactPhone(BaseModel):
    phone = models.CharField(max_length=255, null=True, blank=True)
    is_primary_phone = models.BooleanField(default=False, null=True, blank=True)
    is_primary_mobile_no = models.BooleanField(default=False, null=True, blank=True)
