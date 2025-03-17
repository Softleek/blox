from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class CustomHTMLBlock(BaseModel):
    html = models.CharField(max_length=255, null=True, blank=True)
    preview = models.TextField(null=True, blank=True)
    script = models.CharField(max_length=255, null=True, blank=True)
    style = models.CharField(max_length=255, null=True, blank=True)
    js_message = models.TextField(null=True, blank=True)
    roles = models.ManyToManyField("frappe_app.HasRole", related_name="CustomHTMLBlockRoles", )
    private = models.BooleanField(default=False, null=True, blank=True)
