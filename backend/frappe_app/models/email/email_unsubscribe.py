from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EmailUnsubscribe(BaseModel):
    email = models.CharField(max_length=255, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="EmailUnsubscribeReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    global_unsubscribe = models.BooleanField(default=False, null=True, blank=True)
