from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebFormField(BaseModel):
    CHOICES_FIELDNAME = [
        ("", ""),
    ]
    fieldname = models.CharField(choices=CHOICES_FIELDNAME, max_length=255, null=True, blank=True)
    CHOICES_FIELDTYPE = [
        ("Attach", "Attach"),
        ("Attach Image", "Attach Image"),
        ("Check", "Check"),
        ("Currency", "Currency"),
        ("Color", "Color"),
        ("Data", "Data"),
        ("Date", "Date"),
        ("Datetime", "Datetime"),
        ("Duration", "Duration"),
        ("Float", "Float"),
        ("HTML", "HTML"),
        ("Int", "Int"),
        ("Link", "Link"),
        ("Password", "Password"),
        ("Phone", "Phone"),
        ("Rating", "Rating"),
        ("Select", "Select"),
        ("Signature", "Signature"),
        ("Small Text", "Small Text"),
        ("Text", "Text"),
        ("Text Editor", "Text Editor"),
        ("Table", "Table"),
        ("Time", "Time"),
        ("Section Break", "Section Break"),
        ("Column Break", "Column Break"),
        ("Page Break", "Page Break"),
    ]
    fieldtype = models.CharField(choices=CHOICES_FIELDTYPE, max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    allow_read_on_all_link_options = models.BooleanField(default=False, null=True, blank=True)
    reqd = models.BooleanField(default=False, null=True, blank=True)
    depends_on = models.CharField(max_length=255, null=True, blank=True)
    read_only = models.BooleanField(default=False, null=True, blank=True)
    show_in_filter = models.BooleanField(default=False, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)
    options = models.TextField(null=True, blank=True)
    max_length = models.IntegerField(null=True, blank=True)
    max_value = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    default = models.CharField(max_length=255, null=True, blank=True)
    mandatory_depends_on = models.CharField(max_length=255, null=True, blank=True)
    read_only_depends_on = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_PRECISION = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    ]
    precision = models.CharField(choices=CHOICES_PRECISION, max_length=255, null=True, blank=True)
