from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class LogsToClear(BaseModel):
    ref_doctype = models.ForeignKey("frappe_app.Doctype", related_name="LogsToClearRefDoctype", on_delete=models.CASCADE, null=True, blank=True)
    days = models.IntegerField(default=30, null=True, blank=True)
