from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PropertySetter(BaseModel):
    help = models.TextField(null=True, blank=True)
    CHOICES_DOCTYPE_OR_FIELD = [
        ("DocField", "DocField"),
        ("DocType", "DocType"),
        ("DocType Link", "DocType Link"),
        ("DocType Action", "DocType Action"),
        ("DocType State", "DocType State"),
    ]
    doctype_or_field = models.CharField(choices=CHOICES_DOCTYPE_OR_FIELD, max_length=255, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    doc_type = models.ForeignKey("frappe_app.Doctype", related_name="PropertySetterDocType", on_delete=models.CASCADE, null=True, blank=True)
    field_name = models.CharField(max_length=255, null=True, blank=True)
    property = models.CharField(max_length=255, null=True, blank=True)
    property_type = models.CharField(max_length=255, null=True, blank=True)
    default_value = models.CharField(max_length=255, null=True, blank=True)
    row_name = models.CharField(max_length=255, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="PropertySetterModule", on_delete=models.CASCADE, null=True, blank=True)
    is_system_generated = models.BooleanField(default=False, null=True, blank=True)
