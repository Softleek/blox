from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NotificationRecipient(BaseModel):
    cc = models.CharField(max_length=255, null=True, blank=True)
    bcc = models.CharField(max_length=255, null=True, blank=True)
    condition = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_RECEIVER_BY_DOCUMENT_FIELD = [
        ("", ""),
    ]
    receiver_by_document_field = models.CharField(choices=CHOICES_RECEIVER_BY_DOCUMENT_FIELD, max_length=255, null=True, blank=True)
    receiver_by_role = models.ForeignKey("frappe_app.Role", related_name="NotificationRecipientReceiverByRole", on_delete=models.CASCADE, null=True, blank=True)
