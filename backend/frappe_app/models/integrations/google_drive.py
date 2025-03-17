from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class GoogleDrive(SingletonModel):
    enable = models.BooleanField(default=False, null=True, blank=True)
    backup_folder_name = models.CharField(max_length=255, null=True, blank=True)
    authorize_google_drive_access = models.CharField(max_length=255, null=True, blank=True)
    backup_folder_id = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_FREQUENCY = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
    ]
    frequency = models.CharField(choices=CHOICES_FREQUENCY, max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    authorization_code = models.CharField(max_length=255, null=True, blank=True)
    last_backup_on = models.DateTimeField(null=True, blank=True)
    send_email_for_successful_backup = models.BooleanField(default=False, null=True, blank=True)
    file_backup = models.BooleanField(default=False, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
