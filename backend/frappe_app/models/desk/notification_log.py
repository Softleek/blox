from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NotificationLog(BaseModel):
    subject = models.TextField(null=True, blank=True)
    for_user = models.ForeignKey("frappe_app.User", related_name="NotificationLogForUser", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_TYPE = [
        ("Mention", "Mention"),
        ("Energy Point", "Energy Point"),
        ("Assignment", "Assignment"),
        ("Share", "Share"),
        ("Alert", "Alert"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, null=True, blank=True)
    email_content = models.CharField(max_length=255, null=True, blank=True)
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="NotificationLogDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    document_name = models.CharField(max_length=255, null=True, blank=True)
    from_user = models.ForeignKey("frappe_app.User", related_name="NotificationLogFromUser", on_delete=models.CASCADE, null=True, blank=True)
    read = models.BooleanField(default=False, null=True, blank=True)
    open_reference_document = models.CharField(max_length=255, null=True, blank=True)
    attached_file = models.CharField(max_length=255, null=True, blank=True)
    attachment_link = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
