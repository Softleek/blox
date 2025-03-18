from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ReportFilter(BaseModel):
    fieldname = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_FIELDTYPE = [
        ("Check", "Check"),
        ("Currency", "Currency"),
        ("Data", "Data"),
        ("Date", "Date"),
        ("Datetime", "Datetime"),
        ("Dynamic Link", "Dynamic Link"),
        ("Float", "Float"),
        ("Fold", "Fold"),
        ("Int", "Int"),
        ("Link", "Link"),
        ("Select", "Select"),
        ("Time", "Time"),
    ]
    fieldtype = models.CharField(choices=CHOICES_FIELDTYPE, max_length=255, null=True, blank=True)
    mandatory = models.BooleanField(default=False, null=True, blank=True)
    options = models.TextField(null=True, blank=True)
    wildcard_filter = models.BooleanField(default=False, null=True, blank=True)
    default = models.TextField(null=True, blank=True)
