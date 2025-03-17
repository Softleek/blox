from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class UserGroup(BaseModel):
    user_group_members = models.ManyToManyField("frappe_app.UserGroupMember", related_name="UserGroupUserGroupMembers", )
