from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DocShare(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="DocShareUser", on_delete=models.CASCADE, null=True, blank=True)
    share_doctype = models.ForeignKey("frappe_app.Doctype", related_name="DocShareShareDoctype", on_delete=models.CASCADE, null=True, blank=True)
    share_name = models.CharField(max_length=255, null=True, blank=True)
    read = models.BooleanField(default=False, null=True, blank=True)
    write = models.BooleanField(default=False, null=True, blank=True)
    share = models.BooleanField(default=False, null=True, blank=True)
    everyone = models.BooleanField(default=False, null=True, blank=True)
    notify_by_email = models.BooleanField(default=True, null=True, blank=True)
    submit = models.BooleanField(default=False, null=True, blank=True)
