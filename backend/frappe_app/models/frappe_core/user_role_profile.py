from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class UserRoleProfile(BaseModel):
    role_profile = models.ForeignKey("frappe_app.RoleProfile", related_name="UserRoleProfileRoleProfile", on_delete=models.CASCADE, null=True, blank=True)
