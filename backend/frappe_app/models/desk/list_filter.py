from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ListFilter(BaseModel):
    filter_name = models.CharField(max_length=255, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="ListFilterReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    for_user = models.ForeignKey("frappe_app.User", related_name="ListFilterForUser", on_delete=models.CASCADE, null=True, blank=True)
    filters = models.TextField(null=True, blank=True)
