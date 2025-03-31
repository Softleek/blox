from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class OAuthClientRole(BaseModel):
    role = models.ForeignKey("frappe_app.Role", related_name="OAuthClientRoleRole", on_delete=models.CASCADE, null=True, blank=True)
