from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class GoogleContacts(BaseModel):
    enable = models.BooleanField(default=False, null=True, blank=True)
    authorization_code = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    last_sync_on = models.DateTimeField(null=True, blank=True)
    email_id = models.CharField(max_length=255, null=True, blank=True)
    authorize_google_contacts_access = models.CharField(max_length=255, null=True, blank=True)
    next_sync_token = models.CharField(max_length=255, null=True, blank=True)
    pull_from_google_contacts = models.BooleanField(default=False, null=True, blank=True)
    push_to_google_contacts = models.BooleanField(default=False, null=True, blank=True)
