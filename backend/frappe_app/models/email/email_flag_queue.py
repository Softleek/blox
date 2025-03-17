from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EmailFlagQueue(BaseModel):
    is_completed = models.BooleanField(default=False, null=True, blank=True)
    communication = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_ACTION = [
        ("Read", "Read"),
        ("Unread", "Unread"),
    ]
    action = models.CharField(choices=CHOICES_ACTION, max_length=255, null=True, blank=True)
    email_account = models.CharField(max_length=255, null=True, blank=True)
    uid = models.CharField(max_length=255, null=True, blank=True)
