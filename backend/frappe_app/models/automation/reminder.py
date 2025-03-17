from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Reminder(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="ReminderUser", on_delete=models.CASCADE, default='__user', null=True, blank=True)
    reminder_doctype = models.ForeignKey("frappe_app.Doctype", related_name="ReminderReminderDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reminder_docname = models.CharField(max_length=255, null=True, blank=True)
    remind_at = models.DateTimeField(default='now', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    notified = models.BooleanField(default=False, null=True, blank=True)
