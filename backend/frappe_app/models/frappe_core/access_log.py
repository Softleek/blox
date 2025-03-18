from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class AccessLog(BaseModel):
    export_from = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="AccessLogUser", on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(default='Now', null=True, blank=True)
    reference_document = models.CharField(max_length=255, null=True, blank=True)
    file_type = models.CharField(max_length=255, null=True, blank=True)
    report_name = models.CharField(max_length=255, null=True, blank=True)
    page = models.TextField(null=True, blank=True)
    method = models.CharField(max_length=255, null=True, blank=True)
    show_report = models.CharField(max_length=255, null=True, blank=True)
    show_document = models.CharField(max_length=255, null=True, blank=True)
    filters = models.CharField(max_length=255, null=True, blank=True)
    columns = models.TextField(null=True, blank=True)
