from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkspaceQuickList(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="WorkspaceQuickListDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    quick_list_filter = models.CharField(max_length=255, null=True, blank=True)
