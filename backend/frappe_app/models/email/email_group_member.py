from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class EmailGroupMember(BaseModel):
    email_group = models.ForeignKey("frappe_app.EmailGroup", related_name="EmailGroupMemberEmailGroup", on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    unsubscribed = models.BooleanField(default=False, null=True, blank=True)
