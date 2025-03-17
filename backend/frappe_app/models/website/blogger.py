from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Blogger(BaseModel):
    disabled = models.BooleanField(default=False, null=True, blank=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="BloggerUser", on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)
