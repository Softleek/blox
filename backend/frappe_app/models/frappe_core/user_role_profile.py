from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class UserRoleProfile(BaseModel):
    role_profile = models.ForeignKey("frappe_app.RoleProfile", related_name="UserRoleProfileRoleProfile", on_delete=models.CASCADE, null=True, blank=True)
