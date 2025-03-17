from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class GoogleCalendar(BaseModel):
    enable = models.BooleanField(default=True, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="GoogleCalendarUser", on_delete=models.CASCADE, null=True, blank=True)
    calendar_name = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    authorization_code = models.CharField(max_length=255, null=True, blank=True)
    next_sync_token = models.CharField(max_length=255, null=True, blank=True)
    google_calendar_id = models.CharField(max_length=255, null=True, blank=True)
    authorize_google_calendar_access = models.CharField(max_length=255, null=True, blank=True)
    pull_from_google_calendar = models.BooleanField(default=True, null=True, blank=True)
    sync_as_public = models.BooleanField(default=False, null=True, blank=True)
    push_to_google_calendar = models.BooleanField(default=True, null=True, blank=True)
