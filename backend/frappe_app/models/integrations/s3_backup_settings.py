from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class S3BackupSettings(SingletonModel):
    enabled = models.BooleanField(default=False, null=True, blank=True)
    notify_email = models.CharField(max_length=255, null=True, blank=True)
    send_email_for_successful_backup = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_FREQUENCY = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("None", "None"),
    ]
    frequency = models.CharField(choices=CHOICES_FREQUENCY, max_length=255, null=True, blank=True)
    access_key_id = models.CharField(max_length=255, null=True, blank=True)
    secret_access_key = models.CharField(max_length=255, null=True, blank=True)
    endpoint_url = models.CharField(max_length=255, default='https://s3.amazonaws.com', null=True, blank=True)
    bucket = models.CharField(max_length=255, null=True, blank=True)
    backup_files = models.BooleanField(default=True, null=True, blank=True)
