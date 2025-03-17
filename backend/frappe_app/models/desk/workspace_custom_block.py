from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkspaceCustomBlock(BaseModel):
    custom_block_name = models.ForeignKey("frappe_app.CustomHtmlBlock", related_name="WorkspaceCustomBlockCustomBlockName", on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
