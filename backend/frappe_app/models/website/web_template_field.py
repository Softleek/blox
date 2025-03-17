from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebTemplateField(BaseModel):
    label = models.CharField(max_length=255, null=True, blank=True)
    fieldname = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_FIELDTYPE = [
        ("Attach Image", "Attach Image"),
        ("Check", "Check"),
        ("Data", "Data"),
        ("Int", "Int"),
        ("Link", "Link"),
        ("Select", "Select"),
        ("Small Text", "Small Text"),
        ("Text", "Text"),
        ("Markdown Editor", "Markdown Editor"),
        ("Section Break", "Section Break"),
        ("Column Break", "Column Break"),
        ("Table Break", "Table Break"),
    ]
    fieldtype = models.CharField(choices=CHOICES_FIELDTYPE, max_length=255, default='Data', null=True, blank=True)
    reqd = models.BooleanField(default=False, null=True, blank=True)
    options = models.TextField(null=True, blank=True)
    default = models.TextField(null=True, blank=True)
