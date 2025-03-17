from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkspaceLink(BaseModel):
    CHOICES_TYPE = [
        ("Link", "Link"),
        ("Card Break", "Card Break"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, default='Link', null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_LINK_TYPE = [
        ("DocType", "DocType"),
        ("Page", "Page"),
        ("Report", "Report"),
    ]
    link_type = models.CharField(choices=CHOICES_LINK_TYPE, max_length=255, null=True, blank=True)
    link_to = models.CharField(max_length=255, null=True, blank=True)
    dependencies = models.CharField(max_length=255, null=True, blank=True)
    only_for = models.ForeignKey("frappe_app.Country", related_name="WorkspaceLinkOnlyFor", on_delete=models.CASCADE, null=True, blank=True)
    onboard = models.BooleanField(default=False, null=True, blank=True)
    is_query_report = models.BooleanField(default=False, null=True, blank=True)
    link_count = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    report_ref_doctype = models.ForeignKey("frappe_app.Doctype", related_name="WorkspaceLinkReportRefDoctype", on_delete=models.CASCADE, null=True, blank=True)
