from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class IntegrationRequest(BaseModel):
    integration_request_service = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Queued", "Queued"),
        ("Authorized", "Authorized"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
        ("Failed", "Failed"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Queued', null=True, blank=True)
    data = models.CharField(max_length=255, null=True, blank=True)
    output = models.CharField(max_length=255, null=True, blank=True)
    error = models.CharField(max_length=255, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="IntegrationRequestReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_docname = models.CharField(max_length=255, null=True, blank=True)
    is_remote_request = models.BooleanField(default=False, null=True, blank=True)
    request_description = models.CharField(max_length=255, null=True, blank=True)
    request_id = models.CharField(max_length=255, null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    request_headers = models.CharField(max_length=255, null=True, blank=True)
