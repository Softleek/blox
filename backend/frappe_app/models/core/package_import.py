from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PackageImport(BaseModel):
    attach_package = models.CharField(max_length=255, null=True, blank=True)
    activate = models.BooleanField(default=False, null=True, blank=True)
    log = models.CharField(max_length=255, null=True, blank=True)
    force = models.BooleanField(default=False, null=True, blank=True)
