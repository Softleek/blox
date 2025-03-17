from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DeletedDocument(BaseModel):
    deleted_name = models.CharField(max_length=255, null=True, blank=True)
    deleted_doctype = models.CharField(max_length=255, null=True, blank=True)
    restored = models.BooleanField(default=False, null=True, blank=True)
    new_name = models.CharField(max_length=255, null=True, blank=True)
    data = models.CharField(max_length=255, null=True, blank=True)
