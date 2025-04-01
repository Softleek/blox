from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class UserTypeModule(BaseModel):
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="UserTypeModuleModule", on_delete=models.CASCADE, null=True, blank=True)
