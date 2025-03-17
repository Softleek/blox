from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class OAuthAuthorizationCode(BaseModel):
    client = models.ForeignKey("frappe_app.OauthClient", related_name="OAuthAuthorizationCodeClient", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="OAuthAuthorizationCodeUser", on_delete=models.CASCADE, null=True, blank=True)
    scopes = models.TextField(null=True, blank=True)
    authorization_code = models.CharField(max_length=255, null=True, blank=True)
    expiration_time = models.DateTimeField(null=True, blank=True)
    redirect_uri_bound_to_authorization_code = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_VALIDITY = [
        ("Valid", "Valid"),
        ("Invalid", "Invalid"),
    ]
    validity = models.CharField(choices=CHOICES_VALIDITY, max_length=255, null=True, blank=True)
    nonce = models.CharField(max_length=255, null=True, blank=True)
    code_challenge = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_CODE_CHALLENGE_METHOD = [
        ("s256", "s256"),
        ("plain", "plain"),
    ]
    code_challenge_method = models.CharField(choices=CHOICES_CODE_CHALLENGE_METHOD, max_length=255, null=True, blank=True)
