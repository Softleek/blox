from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebhookRequestLog(BaseModel):
    url = models.TextField(null=True, blank=True)
    headers = models.CharField(max_length=255, null=True, blank=True)
    response = models.CharField(max_length=255, null=True, blank=True)
    data = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="WebhookRequestLogUser", on_delete=models.CASCADE, null=True, blank=True)
    reference_document = models.CharField(max_length=255, null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    webhook = models.ForeignKey("frappe_app.Webhook", related_name="WebhookRequestLogWebhook", on_delete=models.CASCADE, null=True, blank=True)
    reference_doctype = models.CharField(max_length=255, null=True, blank=True)
