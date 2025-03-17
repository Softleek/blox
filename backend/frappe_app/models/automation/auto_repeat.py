from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class AutoRepeat(BaseModel):
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="AutoRepeatReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_document = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(default='Today', null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_FREQUENCY = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("Quarterly", "Quarterly"),
        ("Half-yearly", "Half-yearly"),
        ("Yearly", "Yearly"),
    ]
    frequency = models.CharField(choices=CHOICES_FREQUENCY, max_length=255, null=True, blank=True)
    repeat_on_day = models.IntegerField(null=True, blank=True)
    next_schedule_date = models.DateField(null=True, blank=True)
    notify_by_email = models.BooleanField(default=False, null=True, blank=True)
    recipients = models.TextField(null=True, blank=True)
    get_contacts = models.CharField(max_length=255, null=True, blank=True)
    template = models.ForeignKey("frappe_app.EmailTemplate", related_name="AutoRepeatTemplate", on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(default='Please find attached {{ doc.doctype }} #{{ doc.name }}', null=True, blank=True)
    preview_message = models.CharField(max_length=255, null=True, blank=True)
    print_format = models.ForeignKey("frappe_app.PrintFormat", related_name="AutoRepeatPrintFormat", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_STATUS = [
        ("Active", "Active"),
        ("Disabled", "Disabled"),
        ("Completed", "Completed"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
    repeat_on_last_day = models.BooleanField(default=False, null=True, blank=True)
    repeat_on_days = models.ManyToManyField("frappe_app.AutoRepeatDay", related_name="AutoRepeatRepeatOnDays", )
    submit_on_creation = models.BooleanField(default=False, null=True, blank=True)
