from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NotificationSubscribedDocument(BaseModel):
    document = models.ForeignKey("frappe_app.Doctype", related_name="NotificationSubscribedDocumentDocument", on_delete=models.CASCADE, null=True, blank=True)
