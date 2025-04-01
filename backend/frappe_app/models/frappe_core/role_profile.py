from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class RoleProfile(BaseModel):
    role_profile = models.CharField(max_length=255, null=True, blank=True)
    roles_html = models.TextField(null=True, blank=True)
    roles = models.ManyToManyField("frappe_app.HasRole", related_name="RoleProfileRoles", )
