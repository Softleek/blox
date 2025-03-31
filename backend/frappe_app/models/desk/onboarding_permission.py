from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class OnboardingPermission(BaseModel):
    role = models.ForeignKey("frappe_app.Role", related_name="OnboardingPermissionRole", on_delete=models.CASCADE, null=True, blank=True)
