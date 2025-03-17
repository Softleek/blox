from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ServerScript(BaseModel):
    CHOICES_SCRIPT_TYPE = [
        ("DocType Event", "DocType Event"),
        ("Scheduler Event", "Scheduler Event"),
        ("Permission Query", "Permission Query"),
        ("API", "API"),
    ]
    script_type = models.CharField(choices=CHOICES_SCRIPT_TYPE, max_length=255, null=True, blank=True)
    script = models.CharField(max_length=255, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="ServerScriptReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_DOCTYPE_EVENT = [
        ("Before Insert", "Before Insert"),
        ("Before Validate", "Before Validate"),
        ("Before Save", "Before Save"),
        ("After Insert", "After Insert"),
        ("After Save", "After Save"),
        ("Before Rename", "Before Rename"),
        ("After Rename", "After Rename"),
        ("Before Submit", "Before Submit"),
        ("After Submit", "After Submit"),
        ("Before Cancel", "Before Cancel"),
        ("After Cancel", "After Cancel"),
        ("Before Discard", "Before Discard"),
        ("After Discard", "After Discard"),
        ("Before Delete", "Before Delete"),
        ("After Delete", "After Delete"),
        ("Before Save (Submitted Document)", "Before Save (Submitted Document)"),
        ("After Save (Submitted Document)", "After Save (Submitted Document)"),
        ("Before Print", "Before Print"),
        ("On Payment Authorization", "On Payment Authorization"),
        ("On Payment Paid", "On Payment Paid"),
        ("On Payment Failed", "On Payment Failed"),
        ("On Payment Charge Processed", "On Payment Charge Processed"),
        ("On Payment Mandate Charge Processed", "On Payment Mandate Charge Processed"),
        ("On Payment Mandate Acquisition Processed", "On Payment Mandate Acquisition Processed"),
    ]
    doctype_event = models.CharField(choices=CHOICES_DOCTYPE_EVENT, max_length=255, null=True, blank=True)
    api_method = models.CharField(max_length=255, null=True, blank=True)
    allow_guest = models.BooleanField(default=False, null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    help_html = models.TextField(null=True, blank=True)
    CHOICES_EVENT_FREQUENCY = [
        ("All", "All"),
        ("Hourly", "Hourly"),
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("Yearly", "Yearly"),
        ("Hourly Long", "Hourly Long"),
        ("Daily Long", "Daily Long"),
        ("Weekly Long", "Weekly Long"),
        ("Monthly Long", "Monthly Long"),
        ("Cron", "Cron"),
    ]
    event_frequency = models.CharField(choices=CHOICES_EVENT_FREQUENCY, max_length=255, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="ServerScriptModule", on_delete=models.CASCADE, null=True, blank=True)
    enable_rate_limit = models.BooleanField(default=False, null=True, blank=True)
    rate_limit_count = models.IntegerField(default=5, null=True, blank=True)
    rate_limit_seconds = models.IntegerField(default=86400, null=True, blank=True)
    cron_format = models.CharField(max_length=255, null=True, blank=True)
