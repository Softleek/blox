from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DocumentShareKey(BaseModel):
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="DocumentShareKeyReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_docname = models.CharField(max_length=255, null=True, blank=True)
    key = models.CharField(max_length=255, null=True, blank=True)
    expires_on = models.DateField(null=True, blank=True)
