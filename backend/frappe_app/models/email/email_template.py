from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class EmailTemplate(BaseModel):
    subject = models.CharField(max_length=255, null=True, blank=True)
    response = models.CharField(max_length=255, null=True, blank=True)
    email_reply_help = models.TextField(null=True, blank=True)
    use_html = models.BooleanField(default=False, null=True, blank=True)
    response_html = models.CharField(max_length=255, null=True, blank=True)
