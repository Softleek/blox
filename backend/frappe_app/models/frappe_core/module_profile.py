from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ModuleProfile(BaseModel):
    module_profile_name = models.CharField(max_length=255, null=True, blank=True)
    module_html = models.TextField(null=True, blank=True)
    block_modules = models.ManyToManyField("frappe_app.BlockModule", related_name="ModuleProfileBlockModules", )
