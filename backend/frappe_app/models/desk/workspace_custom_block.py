from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class WorkspaceCustomBlock(BaseModel):
    custom_block_name = models.ForeignKey("frappe_app.CustomHtmlBlock", related_name="WorkspaceCustomBlockCustomBlockName", on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
