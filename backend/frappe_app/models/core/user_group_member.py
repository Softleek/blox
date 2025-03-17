from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class UserGroupMember(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="UserGroupMemberUser", on_delete=models.CASCADE, null=True, blank=True)
