from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DesktopIcon(BaseModel):
    module_name = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    standard = models.BooleanField(default=False, null=True, blank=True)
    custom = models.BooleanField(default=False, null=True, blank=True)
    app = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)
    blocked = models.BooleanField(default=False, null=True, blank=True)
    force_show = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_TYPE = [
        ("module", "module"),
        ("list", "list"),
        ("link", "link"),
        ("page", "page"),
        ("query-report", "query-report"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, null=True, blank=True)
    _doctype = models.ForeignKey("frappe_app.Doctype", related_name="DesktopIconDoctype", on_delete=models.CASCADE, null=True, blank=True)
    _report = models.ForeignKey("frappe_app.Report", related_name="DesktopIconReport", on_delete=models.CASCADE, null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    reverse = models.BooleanField(default=False, null=True, blank=True)
    idx = models.IntegerField(null=True, blank=True)
