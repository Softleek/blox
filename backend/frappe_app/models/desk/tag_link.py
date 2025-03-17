from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class TagLink(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    tag = models.ForeignKey("frappe_app.Tag", related_name="TagLinkTag", on_delete=models.CASCADE, null=True, blank=True)
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="TagLinkDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    document_name = models.CharField(max_length=255, null=True, blank=True)
