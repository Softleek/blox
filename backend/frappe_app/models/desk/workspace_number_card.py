from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkspaceNumberCard(BaseModel):
    number_card_name = models.ForeignKey("frappe_app.NumberCard", related_name="WorkspaceNumberCardNumberCardName", on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
