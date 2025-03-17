from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class AutoEmailReport(BaseModel):
    report = models.ForeignKey("frappe_app.Report", related_name="AutoEmailReportReport", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="AutoEmailReportUser", on_delete=models.CASCADE, default='User', null=True, blank=True)
    enabled = models.BooleanField(default=True, null=True, blank=True)
    report_type = models.CharField(max_length=255, null=True, blank=True)
    send_if_data = models.BooleanField(default=True, null=True, blank=True)
    data_modified_till = models.IntegerField(null=True, blank=True)
    no_of_rows = models.IntegerField(default=100, null=True, blank=True)
    filters_display = models.TextField(null=True, blank=True)
    filters = models.TextField(null=True, blank=True)
    filter_meta = models.TextField(null=True, blank=True)
    CHOICES_FROM_DATE_FIELD = [
        ("", ""),
    ]
    from_date_field = models.CharField(choices=CHOICES_FROM_DATE_FIELD, max_length=255, null=True, blank=True)
    CHOICES_TO_DATE_FIELD = [
        ("", ""),
    ]
    to_date_field = models.CharField(choices=CHOICES_TO_DATE_FIELD, max_length=255, null=True, blank=True)
    CHOICES_DYNAMIC_DATE_PERIOD = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("Quarterly", "Quarterly"),
        ("Half Yearly", "Half Yearly"),
        ("Yearly", "Yearly"),
    ]
    dynamic_date_period = models.CharField(choices=CHOICES_DYNAMIC_DATE_PERIOD, max_length=255, null=True, blank=True)
    email_to = models.TextField(null=True, blank=True)
    CHOICES_DAY_OF_WEEK = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    day_of_week = models.CharField(choices=CHOICES_DAY_OF_WEEK, max_length=255, default='Monday', null=True, blank=True)
    CHOICES_FREQUENCY = [
        ("Daily", "Daily"),
        ("Weekdays", "Weekdays"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
    ]
    frequency = models.CharField(choices=CHOICES_FREQUENCY, max_length=255, null=True, blank=True)
    CHOICES_FORMAT = [
        ("HTML", "HTML"),
        ("XLSX", "XLSX"),
        ("CSV", "CSV"),
    ]
    format = models.CharField(choices=CHOICES_FORMAT, max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    reference_report = models.CharField(max_length=255, null=True, blank=True)
    sender = models.ForeignKey("frappe_app.EmailAccount", related_name="AutoEmailReportSender", on_delete=models.CASCADE, null=True, blank=True)
    use_first_day_of_period = models.BooleanField(default=False, null=True, blank=True)
