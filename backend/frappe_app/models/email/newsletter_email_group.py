from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NewsletterEmailGroup(BaseModel):
    email_group = models.ForeignKey("frappe_app.EmailGroup", related_name="NewsletterEmailGroupEmailGroup", on_delete=models.CASCADE, null=True, blank=True)
    total_subscribers = models.CharField(max_length=255, null=True, blank=True)
