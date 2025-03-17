from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EmailQueueRecipient(BaseModel):
    recipient = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Not Sent", "Not Sent"),
        ("Sent", "Sent"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Not Sent', null=True, blank=True)
    error = models.CharField(max_length=255, null=True, blank=True)
