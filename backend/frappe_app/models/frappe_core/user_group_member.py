from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class UserGroupMember(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="UserGroupMemberUser", on_delete=models.CASCADE, null=True, blank=True)
