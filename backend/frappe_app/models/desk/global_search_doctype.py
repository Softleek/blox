from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class GlobalSearchDocType(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="GlobalSearchDocTypeDocumentType", on_delete=models.CASCADE, null=True, blank=True)
