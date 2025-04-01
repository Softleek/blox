from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class UserGroup(BaseModel):
    user_group_members = models.ManyToManyField("frappe_app.UserGroupMember", related_name="UserGroupUserGroupMembers", )
