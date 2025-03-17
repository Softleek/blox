from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ReportColumn(BaseModel):
    fieldname = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_FIELDTYPE = [
        ("Check", "Check"),
        ("Currency", "Currency"),
        ("Data", "Data"),
        ("Date", "Date"),
        ("Datetime", "Datetime"),
        ("Duration", "Duration"),
        ("Dynamic Link", "Dynamic Link"),
        ("Float", "Float"),
        ("Fold", "Fold"),
        ("Int", "Int"),
        ("Link", "Link"),
        ("Select", "Select"),
        ("Time", "Time"),
    ]
    fieldtype = models.CharField(choices=CHOICES_FIELDTYPE, max_length=255, null=True, blank=True)
    options = models.CharField(max_length=255, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
