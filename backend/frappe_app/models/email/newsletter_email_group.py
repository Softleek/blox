from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class NewsletterEmailGroup(BaseModel):
    email_group = models.ForeignKey("frappe_app.EmailGroup", related_name="NewsletterEmailGroupEmailGroup", on_delete=models.CASCADE, null=True, blank=True)
    total_subscribers = models.CharField(max_length=255, null=True, blank=True)
