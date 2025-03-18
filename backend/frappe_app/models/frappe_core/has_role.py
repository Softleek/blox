from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class HasRole(BaseModel):
    role = models.ForeignKey("frappe_app.Role", related_name="HasRoleRole", on_delete=models.CASCADE, null=True, blank=True)
