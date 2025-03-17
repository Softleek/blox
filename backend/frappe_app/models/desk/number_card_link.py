from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NumberCardLink(BaseModel):
    card = models.ForeignKey("frappe_app.NumberCard", related_name="NumberCardLinkCard", on_delete=models.CASCADE, null=True, blank=True)
