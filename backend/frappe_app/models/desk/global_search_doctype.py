from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class GlobalSearchDocType(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="GlobalSearchDocTypeDocumentType", on_delete=models.CASCADE, null=True, blank=True)
