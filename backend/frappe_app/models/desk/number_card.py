from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NumberCard(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="NumberCardDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_FUNCTION = [
        ("Count", "Count"),
        ("Sum", "Sum"),
        ("Average", "Average"),
        ("Minimum", "Minimum"),
        ("Maximum", "Maximum"),
    ]
    function = models.CharField(choices=CHOICES_FUNCTION, max_length=255, null=True, blank=True)
    CHOICES_AGGREGATE_FUNCTION_BASED_ON = [
        ("", ""),
    ]
    aggregate_function_based_on = models.CharField(choices=CHOICES_AGGREGATE_FUNCTION_BASED_ON, max_length=255, null=True, blank=True)
    filters_json = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    is_public = models.BooleanField(default=False, null=True, blank=True)
    show_percentage_stats = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_STATS_TIME_INTERVAL = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("Yearly", "Yearly"),
    ]
    stats_time_interval = models.CharField(choices=CHOICES_STATS_TIME_INTERVAL, max_length=255, default='Daily', null=True, blank=True)
    is_standard = models.BooleanField(default=False, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="NumberCardModule", on_delete=models.CASCADE, null=True, blank=True)
    dynamic_filters_json = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_TYPE = [
        ("Document Type", "Document Type"),
        ("Report", "Report"),
        ("Custom", "Custom"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, null=True, blank=True)
    report_name = models.ForeignKey("frappe_app.Report", related_name="NumberCardReportName", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_REPORT_FIELD = [
        ("", ""),
    ]
    report_field = models.CharField(choices=CHOICES_REPORT_FIELD, max_length=255, null=True, blank=True)
    method = models.CharField(max_length=255, null=True, blank=True)
    filters_config = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_REPORT_FUNCTION = [
        ("Sum", "Sum"),
        ("Average", "Average"),
        ("Minimum", "Minimum"),
        ("Maximum", "Maximum"),
    ]
    report_function = models.CharField(choices=CHOICES_REPORT_FUNCTION, max_length=255, null=True, blank=True)
    parent_document_type = models.ForeignKey("frappe_app.Doctype", related_name="NumberCardParentDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    currency = models.ForeignKey("frappe_app.Currency", related_name="NumberCardCurrency", on_delete=models.CASCADE, null=True, blank=True)
