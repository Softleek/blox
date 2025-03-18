from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class UserDocumentType(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="UserDocumentTypeDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    read = models.BooleanField(default=True, null=True, blank=True)
    write = models.BooleanField(default=False, null=True, blank=True)
    create = models.BooleanField(default=False, null=True, blank=True)
    is_custom = models.BooleanField(default=False, null=True, blank=True)
    submit = models.BooleanField(default=False, null=True, blank=True)
    cancel = models.BooleanField(default=False, null=True, blank=True)
    amend = models.BooleanField(default=False, null=True, blank=True)
    delete = models.BooleanField(default=False, null=True, blank=True)
    email = models.BooleanField(default=True, null=True, blank=True)
    share = models.BooleanField(default=True, null=True, blank=True)
    print = models.BooleanField(default=True, null=True, blank=True)
