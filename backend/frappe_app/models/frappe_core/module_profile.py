from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class ModuleProfile(BaseModel):
    module_profile_name = models.CharField(max_length=255, null=True, blank=True)
    module_html = models.TextField(null=True, blank=True)
    block_modules = models.ManyToManyField("frappe_app.BlockModule", related_name="ModuleProfileBlockModules", )
