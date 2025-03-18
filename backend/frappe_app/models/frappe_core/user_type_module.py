from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class UserTypeModule(BaseModel):
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="UserTypeModuleModule", on_delete=models.CASCADE, null=True, blank=True)
