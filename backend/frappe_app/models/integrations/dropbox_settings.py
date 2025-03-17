from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DropboxSettings(SingletonModel):
    enabled = models.BooleanField(default=False, null=True, blank=True)
    send_notifications_to = models.CharField(max_length=255, null=True, blank=True)
    send_email_for_successful_backup = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_BACKUP_FREQUENCY = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
    ]
    backup_frequency = models.CharField(choices=CHOICES_BACKUP_FREQUENCY, max_length=255, null=True, blank=True)
    limit_no_of_backups = models.BooleanField(default=False, null=True, blank=True)
    no_of_backups = models.IntegerField(default=5, null=True, blank=True)
    file_backup = models.BooleanField(default=True, null=True, blank=True)
    app_access_key = models.CharField(max_length=255, null=True, blank=True)
    app_secret_key = models.CharField(max_length=255, null=True, blank=True)
    allow_dropbox_access = models.CharField(max_length=255, null=True, blank=True)
    dropbox_refresh_token = models.CharField(max_length=255, null=True, blank=True)
    dropbox_access_token = models.CharField(max_length=255, null=True, blank=True)
