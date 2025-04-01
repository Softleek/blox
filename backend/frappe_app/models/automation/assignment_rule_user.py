from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class AssignmentRuleUser(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="AssignmentRuleUserUser", on_delete=models.CASCADE, null=True, blank=True)
