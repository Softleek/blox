from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class File(BaseModel):
    file_name = models.CharField(max_length=255, null=True, blank=True)
    is_private = models.BooleanField(default=False, null=True, blank=True)
    preview_html = models.TextField(null=True, blank=True)
    is_home_folder = models.BooleanField(default=False, null=True, blank=True)
    is_attachments_folder = models.BooleanField(default=False, null=True, blank=True)
    file_size = models.IntegerField(null=True, blank=True)
    file_url = models.CharField(max_length=255, null=True, blank=True)
    thumbnail_url = models.TextField(null=True, blank=True)
    folder = models.ForeignKey("frappe_app.File", related_name="FileFolder", on_delete=models.CASCADE, null=True, blank=True)
    is_folder = models.BooleanField(default=False, null=True, blank=True)
    attached_to_doctype = models.ForeignKey("frappe_app.Doctype", related_name="FileAttachedToDoctype", on_delete=models.CASCADE, null=True, blank=True)
    attached_to_name = models.CharField(max_length=255, null=True, blank=True)
    attached_to_field = models.CharField(max_length=255, null=True, blank=True)
    old_parent = models.CharField(max_length=255, null=True, blank=True)
    content_hash = models.CharField(max_length=255, null=True, blank=True)
    uploaded_to_dropbox = models.BooleanField(default=False, null=True, blank=True)
    uploaded_to_google_drive = models.BooleanField(default=False, null=True, blank=True)
    file_type = models.CharField(max_length=255, null=True, blank=True)
