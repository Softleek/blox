from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class RouteHistory(BaseModel):
    route = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="RouteHistoryUser", on_delete=models.CASCADE, null=True, blank=True)
