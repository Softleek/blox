from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class TransactionLog(BaseModel):
    row_index = models.CharField(max_length=255, null=True, blank=True)
    reference_doctype = models.CharField(max_length=255, null=True, blank=True)
    document_name = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    checksum_version = models.CharField(max_length=255, null=True, blank=True)
    previous_hash = models.TextField(null=True, blank=True)
    transaction_hash = models.TextField(null=True, blank=True)
    chaining_hash = models.TextField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    amended_from = models.ForeignKey("frappe_app.TransactionLog", related_name="TransactionLogAmendedFrom", on_delete=models.CASCADE, null=True, blank=True)
