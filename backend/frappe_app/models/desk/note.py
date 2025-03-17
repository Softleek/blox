from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Note(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    public = models.BooleanField(default=False, null=True, blank=True)
    notify_on_login = models.BooleanField(default=False, null=True, blank=True)
    notify_on_every_login = models.BooleanField(default=False, null=True, blank=True)
    expire_notification_on = models.DateField(null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    seen_by = models.ManyToManyField("frappe_app.NoteSeenBy", related_name="NoteSeenBy", )
