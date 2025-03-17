from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebsiteRouteRedirect(BaseModel):
    source = models.TextField(null=True, blank=True)
    target = models.TextField(null=True, blank=True)
    CHOICES_REDIRECT_HTTP_STATUS = [
        ("301", "301"),
        ("302", "302"),
        ("307", "307"),
        ("308", "308"),
    ]
    redirect_http_status = models.CharField(choices=CHOICES_REDIRECT_HTTP_STATUS, max_length=255, default='301', null=True, blank=True)
