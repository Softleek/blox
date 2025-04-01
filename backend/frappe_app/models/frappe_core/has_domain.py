from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class HasDomain(BaseModel):
    domain = models.ForeignKey("frappe_app.Domain", related_name="HasDomainDomain", on_delete=models.CASCADE, null=True, blank=True)
