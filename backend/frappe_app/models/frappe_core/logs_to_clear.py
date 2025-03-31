from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class LogsToClear(BaseModel):
    ref_doctype = models.ForeignKey("frappe_app.Doctype", related_name="LogsToClearRefDoctype", on_delete=models.CASCADE, null=True, blank=True)
    days = models.IntegerField(default=30, null=True, blank=True)
