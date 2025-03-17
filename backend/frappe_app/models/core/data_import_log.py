from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DataImportLog(BaseModel):
    data_import = models.ForeignKey("frappe_app.DataImport", related_name="DataImportLogDataImport", on_delete=models.CASCADE, null=True, blank=True)
    docname = models.CharField(max_length=255, null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
    row_indexes = models.CharField(max_length=255, null=True, blank=True)
    success = models.BooleanField(default=False, null=True, blank=True)
    log_index = models.IntegerField(null=True, blank=True)
    messages = models.CharField(max_length=255, null=True, blank=True)
