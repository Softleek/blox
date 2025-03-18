from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Version(BaseModel):
    ref_doctype = models.ForeignKey("frappe_app.Doctype", related_name="VersionRefDoctype", on_delete=models.CASCADE, null=True, blank=True)
    docname = models.CharField(max_length=255, null=True, blank=True)
    data = models.CharField(max_length=255, null=True, blank=True)
    table_html = models.TextField(null=True, blank=True)
