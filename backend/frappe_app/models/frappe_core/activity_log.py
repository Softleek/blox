from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ActivityLog(BaseModel):
    subject = models.TextField(null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    communication_date = models.DateTimeField(default='Now', null=True, blank=True)
    CHOICES_OPERATION = [
        ("Login", "Login"),
        ("Logout", "Logout"),
        ("Impersonate", "Impersonate"),
    ]
    operation = models.CharField(choices=CHOICES_OPERATION, max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Success", "Success"),
        ("Failed", "Failed"),
        ("Linked", "Linked"),
        ("Closed", "Closed"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="ActivityLogReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    reference_owner = models.CharField(max_length=255, null=True, blank=True)
    timeline_doctype = models.ForeignKey("frappe_app.Doctype", related_name="ActivityLogTimelineDoctype", on_delete=models.CASCADE, null=True, blank=True)
    timeline_name = models.CharField(max_length=255, null=True, blank=True)
    link_doctype = models.ForeignKey("frappe_app.Doctype", related_name="ActivityLogLinkDoctype", on_delete=models.CASCADE, null=True, blank=True)
    link_name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="ActivityLogUser", on_delete=models.CASCADE, default='__user', null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
