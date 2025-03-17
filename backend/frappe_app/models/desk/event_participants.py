from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EventParticipants(BaseModel):
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="EventParticipantsReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_docname = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
