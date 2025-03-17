from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class OAuthClient(BaseModel):
    client_id = models.CharField(max_length=255, null=True, blank=True)
    app_name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="OAuthClientUser", on_delete=models.CASCADE, null=True, blank=True)
    client_secret = models.CharField(max_length=255, null=True, blank=True)
    skip_authorization = models.BooleanField(default=False, null=True, blank=True)
    scopes = models.TextField(default='all openid', null=True, blank=True)
    redirect_uris = models.TextField(null=True, blank=True)
    default_redirect_uri = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_GRANT_TYPE = [
        ("Authorization Code", "Authorization Code"),
        ("Implicit", "Implicit"),
    ]
    grant_type = models.CharField(choices=CHOICES_GRANT_TYPE, max_length=255, null=True, blank=True)
    CHOICES_RESPONSE_TYPE = [
        ("Code", "Code"),
        ("Token", "Token"),
    ]
    response_type = models.CharField(choices=CHOICES_RESPONSE_TYPE, max_length=255, default='Code', null=True, blank=True)
    allowed_roles = models.ManyToManyField("frappe_app.OauthClientRole", related_name="OAuthClientAllowedRoles", )
