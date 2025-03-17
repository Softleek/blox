from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class OAuthProviderSettings(SingletonModel):
    CHOICES_SKIP_AUTHORIZATION = [
        ("Force", "Force"),
        ("Auto", "Auto"),
    ]
    skip_authorization = models.CharField(choices=CHOICES_SKIP_AUTHORIZATION, max_length=255, null=True, blank=True)
