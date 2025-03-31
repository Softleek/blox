from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class PrintHeading(BaseModel):
    print_heading = models.CharField(max_length=255, null=True, blank=True)
    print_heading.allow_on_submit = True
    description = models.TextField(null=True, blank=True)
