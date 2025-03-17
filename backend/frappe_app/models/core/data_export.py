from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DataExport(SingletonModel):
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="DataExportReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_FILE_TYPE = [
        ("Excel", "Excel"),
        ("CSV", "CSV"),
    ]
    file_type = models.CharField(choices=CHOICES_FILE_TYPE, max_length=255, default='CSV', null=True, blank=True)
    filter_list = models.TextField(null=True, blank=True)
    fields_multicheck = models.TextField(null=True, blank=True)
    export_without_main_header = models.BooleanField(default=False, null=True, blank=True)
