from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class UnhandledEmail(BaseModel):
    email_account = models.ForeignKey("frappe_app.EmailAccount", related_name="UnhandledEmailEmailAccount", on_delete=models.CASCADE, null=True, blank=True)
    uid = models.CharField(max_length=255, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    message_id = models.CharField(max_length=255, null=True, blank=True)
    raw = models.CharField(max_length=255, null=True, blank=True)
