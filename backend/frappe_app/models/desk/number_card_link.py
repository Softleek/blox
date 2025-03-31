from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class NumberCardLink(BaseModel):
    card = models.ForeignKey("frappe_app.NumberCard", related_name="NumberCardLinkCard", on_delete=models.CASCADE, null=True, blank=True)
