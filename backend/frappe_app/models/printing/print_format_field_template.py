from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PrintFormatFieldTemplate(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="PrintFormatFieldTemplateDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    field = models.CharField(max_length=255, null=True, blank=True)
    template = models.CharField(max_length=255, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="PrintFormatFieldTemplateModule", on_delete=models.CASCADE, null=True, blank=True)
    standard = models.BooleanField(default=False, null=True, blank=True)
    template_file = models.CharField(max_length=255, null=True, blank=True)
