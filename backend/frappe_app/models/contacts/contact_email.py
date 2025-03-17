from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ContactEmail(BaseModel):
    email_id = models.CharField(max_length=255, null=True, blank=True)
    is_primary = models.BooleanField(default=False, null=True, blank=True)
