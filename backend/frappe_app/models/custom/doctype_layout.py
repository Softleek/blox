from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DocTypeLayout(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="DocTypeLayoutDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    fields = models.ManyToManyField("frappe_app.DoctypeLayoutField", related_name="DocTypeLayoutFields", )
    client_script = models.CharField(max_length=255, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
