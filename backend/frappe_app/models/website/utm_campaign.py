from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class UTMCampaign(BaseModel):
    campaign_description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=255, null=True, blank=True)
