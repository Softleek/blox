from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class TokenCache(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="TokenCacheUser", on_delete=models.CASCADE, null=True, blank=True)
    connected_app = models.ForeignKey("frappe_app.ConnectedApp", related_name="TokenCacheConnectedApp", on_delete=models.CASCADE, null=True, blank=True)
    access_token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    expires_in = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    scopes = models.ManyToManyField("frappe_app.OauthScope", related_name="TokenCacheScopes", )
    success_uri = models.CharField(max_length=255, null=True, blank=True)
    token_type = models.CharField(max_length=255, null=True, blank=True)
    provider_name = models.CharField(max_length=255, null=True, blank=True)
