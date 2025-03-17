from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class CommunicationLink(BaseModel):
    link_doctype = models.ForeignKey("frappe_app.Doctype", related_name="CommunicationLinkLinkDoctype", on_delete=models.CASCADE, null=True, blank=True)
    link_name = models.CharField(max_length=255, null=True, blank=True)
    link_title = models.CharField(max_length=255, null=True, blank=True)
