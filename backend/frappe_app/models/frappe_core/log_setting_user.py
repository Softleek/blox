from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class LogSettingUser(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="LogSettingUserUser", on_delete=models.CASCADE, null=True, blank=True)
