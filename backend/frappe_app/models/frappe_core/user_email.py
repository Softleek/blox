from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class UserEmail(BaseModel):
    email_account = models.ForeignKey("frappe_app.EmailAccount", related_name="UserEmailEmailAccount", on_delete=models.CASCADE, null=True, blank=True)
    email_id = models.CharField(max_length=255, null=True, blank=True)
    awaiting_password = models.BooleanField(default=False, null=True, blank=True)
    enable_outgoing = models.BooleanField(default=False, null=True, blank=True)
    used_oauth = models.BooleanField(default=False, null=True, blank=True)
