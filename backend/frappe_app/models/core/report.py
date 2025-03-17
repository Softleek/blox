from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Report(BaseModel):
    report_name = models.CharField(max_length=255, null=True, blank=True)
    ref_doctype = models.ForeignKey("frappe_app.Doctype", related_name="ReportRefDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_report = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_IS_STANDARD = [
        ("No", "No"),
        ("Yes", "Yes"),
    ]
    is_standard = models.CharField(choices=CHOICES_IS_STANDARD, max_length=255, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="ReportModule", on_delete=models.CASCADE, null=True, blank=True)
    add_total_row = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_REPORT_TYPE = [
        ("Report Builder", "Report Builder"),
        ("Query Report", "Query Report"),
        ("Script Report", "Script Report"),
        ("Custom Report", "Custom Report"),
    ]
    report_type = models.CharField(choices=CHOICES_REPORT_TYPE, max_length=255, null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    letter_head = models.ForeignKey("frappe_app.LetterHead", related_name="ReportLetterHead", on_delete=models.CASCADE, null=True, blank=True)
    query = models.CharField(max_length=255, null=True, blank=True)
    javascript = models.CharField(max_length=255, null=True, blank=True)
    json = models.CharField(max_length=255, null=True, blank=True)
    roles = models.ManyToManyField("frappe_app.HasRole", related_name="ReportRoles", )
    prepared_report = models.BooleanField(default=False, null=True, blank=True)
    report_script = models.CharField(max_length=255, null=True, blank=True)
    filters = models.ManyToManyField("frappe_app.ReportFilter", related_name="ReportFilters", )
    columns = models.ManyToManyField("frappe_app.ReportColumn", related_name="ReportColumns", )
    timeout = models.IntegerField(null=True, blank=True)
    add_translate_data = models.BooleanField(default=False, null=True, blank=True)
