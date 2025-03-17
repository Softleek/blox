from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class AddressTemplate(BaseModel):
    country = models.ForeignKey("frappe_app.Country", related_name="AddressTemplateCountry", on_delete=models.CASCADE, null=True, blank=True)
    is_default = models.BooleanField(default=False, null=True, blank=True)
    template = models.CharField(max_length=255, null=True, blank=True)
