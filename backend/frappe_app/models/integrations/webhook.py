from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Webhook(BaseModel):
    webhook_doctype = models.ForeignKey("frappe_app.Doctype", related_name="WebhookWebhookDoctype", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_WEBHOOK_DOCEVENT = [
        ("after_insert", "after_insert"),
        ("on_update", "on_update"),
        ("on_submit", "on_submit"),
        ("on_cancel", "on_cancel"),
        ("on_trash", "on_trash"),
        ("on_update_after_submit", "on_update_after_submit"),
        ("on_change", "on_change"),
    ]
    webhook_docevent = models.CharField(choices=CHOICES_WEBHOOK_DOCEVENT, max_length=255, null=True, blank=True)
    condition = models.TextField(null=True, blank=True)
    html_condition = models.TextField(null=True, blank=True)
    request_url = models.TextField(null=True, blank=True)
    webhook_headers = models.ManyToManyField("frappe_app.WebhookHeader", related_name="WebhookWebhookHeaders", )
    webhook_data = models.ManyToManyField("frappe_app.WebhookData", related_name="WebhookWebhookData", )
    CHOICES_REQUEST_STRUCTURE = [
        ("Form URL-Encoded", "Form URL-Encoded"),
        ("JSON", "JSON"),
    ]
    request_structure = models.CharField(choices=CHOICES_REQUEST_STRUCTURE, max_length=255, null=True, blank=True)
    webhook_json = models.CharField(max_length=255, null=True, blank=True)
    enable_security = models.BooleanField(default=False, null=True, blank=True)
    webhook_secret = models.CharField(max_length=255, null=True, blank=True)
    enabled = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_REQUEST_METHOD = [
        ("POST", "POST"),
        ("PUT", "PUT"),
        ("DELETE", "DELETE"),
    ]
    request_method = models.CharField(choices=CHOICES_REQUEST_METHOD, max_length=255, default='POST', null=True, blank=True)
    is_dynamic_url = models.BooleanField(default=False, null=True, blank=True)
    timeout = models.IntegerField(default=5, null=True, blank=True)
    background_jobs_queue = models.CharField(max_length=255, null=True, blank=True)
