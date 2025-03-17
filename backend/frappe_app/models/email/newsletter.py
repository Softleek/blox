from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Newsletter(BaseModel):
    email_group = models.ManyToManyField("frappe_app.NewsletterEmailGroup", related_name="NewsletterEmailGroup", )
    send_from = models.CharField(max_length=255, null=True, blank=True)
    email_sent = models.BooleanField(default=False, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    send_unsubscribe_link = models.BooleanField(default=True, null=True, blank=True)
    published = models.BooleanField(default=False, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    scheduled_to_send = models.IntegerField(null=True, blank=True)
    schedule_send = models.DateTimeField(null=True, blank=True)
    CHOICES_CONTENT_TYPE = [
        ("Rich Text", "Rich Text"),
        ("Markdown", "Markdown"),
        ("HTML", "HTML"),
    ]
    content_type = models.CharField(choices=CHOICES_CONTENT_TYPE, max_length=255, null=True, blank=True)
    message_md = models.TextField(null=True, blank=True)
    message_html = models.TextField(null=True, blank=True)
    schedule_sending = models.BooleanField(default=False, null=True, blank=True)
    send_webview_link = models.BooleanField(default=False, null=True, blank=True)
    sender_name = models.CharField(max_length=255, null=True, blank=True)
    sender_email = models.CharField(max_length=255, null=True, blank=True)
    attachments = models.ManyToManyField("frappe_app.NewsletterAttachment", related_name="NewsletterAttachments", )
    email_sent_at = models.DateTimeField(null=True, blank=True)
    total_recipients = models.IntegerField(null=True, blank=True)
    total_views = models.IntegerField(default=0, null=True, blank=True)
    campaign = models.ForeignKey("frappe_app.UtmCampaign", related_name="NewsletterCampaign", on_delete=models.CASCADE, null=True, blank=True)
