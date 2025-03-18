from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DocTypeLink(BaseModel):
    link_doctype = models.ForeignKey("frappe_app.Doctype", related_name="DocTypeLinkLinkDoctype", on_delete=models.CASCADE, null=True, blank=True)
    link_fieldname = models.CharField(max_length=255, null=True, blank=True)
    group = models.CharField(max_length=255, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)
    custom = models.BooleanField(default=False, null=True, blank=True)
    parent_doctype = models.ForeignKey("frappe_app.Doctype", related_name="DocTypeLinkParentDoctype", on_delete=models.CASCADE, null=True, blank=True)
    is_child_table = models.BooleanField(default=False, null=True, blank=True)
    table_fieldname = models.CharField(max_length=255, null=True, blank=True)
