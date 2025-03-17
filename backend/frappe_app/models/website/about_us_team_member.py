from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class AboutUsTeamMember(BaseModel):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    image_link = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
