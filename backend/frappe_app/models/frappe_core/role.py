from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Role(BaseModel):
    role_name = models.CharField(max_length=255, null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    desk_access = models.BooleanField(default=True, null=True, blank=True)
    two_factor_auth = models.BooleanField(default=False, null=True, blank=True)
    restrict_to_domain = models.ForeignKey("frappe_app.Domain", related_name="RoleRestrictToDomain", on_delete=models.CASCADE, null=True, blank=True)
    home_page = models.CharField(max_length=255, null=True, blank=True)
    is_custom = models.BooleanField(default=False, null=True, blank=True)
