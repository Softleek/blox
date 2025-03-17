from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NotificationSettings(BaseModel):
    enabled = models.BooleanField(default=True, null=True, blank=True)
    subscribed_documents = models.ManyToManyField("frappe_app.NotificationSubscribedDocument", related_name="NotificationSettingsSubscribedDocuments", )
    enable_email_notifications = models.BooleanField(default=True, null=True, blank=True)
    enable_email_mention = models.BooleanField(default=True, null=True, blank=True)
    enable_email_assignment = models.BooleanField(default=True, null=True, blank=True)
    enable_email_energy_point = models.BooleanField(default=True, null=True, blank=True)
    enable_email_share = models.BooleanField(default=True, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="NotificationSettingsUser", on_delete=models.CASCADE, default='__user', null=True, blank=True)
    seen = models.BooleanField(default=False, null=True, blank=True)
    energy_points_system_notifications = models.BooleanField(default=True, null=True, blank=True)
    enable_email_event_reminders = models.BooleanField(default=True, null=True, blank=True)
    enable_email_threads_on_assigned_document = models.BooleanField(default=True, null=True, blank=True)
