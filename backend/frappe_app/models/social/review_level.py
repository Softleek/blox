from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ReviewLevel(BaseModel):
    level_name = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey("frappe_app.Role", related_name="ReviewLevelRole", on_delete=models.CASCADE, null=True, blank=True)
    review_points = models.IntegerField(null=True, blank=True)
