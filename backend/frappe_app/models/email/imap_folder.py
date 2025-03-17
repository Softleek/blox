from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class IMAPFolder(BaseModel):
    folder_name = models.CharField(max_length=255, null=True, blank=True)
    append_to = models.ForeignKey("frappe_app.Doctype", related_name="IMAPFolderAppendTo", on_delete=models.CASCADE, null=True, blank=True)
    uidvalidity = models.CharField(max_length=255, null=True, blank=True)
    uidnext = models.CharField(max_length=255, null=True, blank=True)
