from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DataImport(BaseModel):
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="DataImportReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_IMPORT_TYPE = [
        ("Insert New Records", "Insert New Records"),
        ("Update Existing Records", "Update Existing Records"),
    ]
    import_type = models.CharField(choices=CHOICES_IMPORT_TYPE, max_length=255, null=True, blank=True)
    import_file = models.CharField(max_length=255, null=True, blank=True)
    import_preview = models.TextField(null=True, blank=True)
    template_options = models.CharField(max_length=255, null=True, blank=True)
    import_log_preview = models.TextField(null=True, blank=True)
    CHOICES_STATUS = [
        ("Pending", "Pending"),
        ("Success", "Success"),
        ("Partial Success", "Partial Success"),
        ("Error", "Error"),
        ("Timed Out", "Timed Out"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Pending', null=True, blank=True)
    template_warnings = models.CharField(max_length=255, null=True, blank=True)
    submit_after_import = models.BooleanField(default=False, null=True, blank=True)
    import_warnings = models.TextField(null=True, blank=True)
    download_template = models.CharField(max_length=255, null=True, blank=True)
    mute_emails = models.BooleanField(default=True, null=True, blank=True)
    show_failed_logs = models.BooleanField(default=False, null=True, blank=True)
    html_5 = models.TextField(null=True, blank=True)
    google_sheets_url = models.CharField(max_length=255, null=True, blank=True)
    refresh_google_sheet = models.CharField(max_length=255, null=True, blank=True)
    payload_count = models.IntegerField(null=True, blank=True)
    delimiter_options = models.CharField(max_length=255, default=',;\\t|', null=True, blank=True)
    custom_delimiters = models.BooleanField(default=False, null=True, blank=True)
    use_csv_sniffer = models.BooleanField(default=False, null=True, blank=True)
