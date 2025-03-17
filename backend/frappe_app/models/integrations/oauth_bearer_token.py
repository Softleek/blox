from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class OAuthBearerToken(BaseModel):
    client = models.ForeignKey("frappe_app.OauthClient", related_name="OAuthBearerTokenClient", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="OAuthBearerTokenUser", on_delete=models.CASCADE, null=True, blank=True)
    scopes = models.TextField(null=True, blank=True)
    access_token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    expiration_time = models.DateTimeField(null=True, blank=True)
    expires_in = models.IntegerField(null=True, blank=True)
    CHOICES_STATUS = [
        ("Active", "Active"),
        ("Revoked", "Revoked"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
