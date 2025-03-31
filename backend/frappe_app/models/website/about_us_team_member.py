from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class AboutUsTeamMember(BaseModel):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    image_link = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
