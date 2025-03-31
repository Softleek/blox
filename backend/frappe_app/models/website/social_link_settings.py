from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class SocialLinkSettings(BaseModel):
    CHOICES_SOCIAL_LINK_TYPE = [
        ("facebook", "facebook"),
        ("linkedin", "linkedin"),
        ("twitter", "twitter"),
        ("email", "email"),
    ]
    social_link_type = models.CharField(choices=CHOICES_SOCIAL_LINK_TYPE, max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    background_color = models.CharField(max_length=255, null=True, blank=True)
