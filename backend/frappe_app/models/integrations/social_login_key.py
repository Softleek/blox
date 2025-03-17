from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SocialLoginKey(BaseModel):
    enable_social_login = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_SOCIAL_LOGIN_PROVIDER = [
        ("Custom", "Custom"),
        ("Facebook", "Facebook"),
        ("Frappe", "Frappe"),
        ("GitHub", "GitHub"),
        ("Google", "Google"),
        ("Office 365", "Office 365"),
        ("Salesforce", "Salesforce"),
        ("fairlogin", "fairlogin"),
        ("Keycloak", "Keycloak"),
    ]
    social_login_provider = models.CharField(choices=CHOICES_SOCIAL_LOGIN_PROVIDER, max_length=255, default='Custom', null=True, blank=True)
    client_id = models.CharField(max_length=255, null=True, blank=True)
    provider_name = models.CharField(max_length=255, null=True, blank=True)
    client_secret = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    base_url = models.CharField(max_length=255, null=True, blank=True)
    authorize_url = models.CharField(max_length=255, null=True, blank=True)
    access_token_url = models.CharField(max_length=255, null=True, blank=True)
    redirect_url = models.CharField(max_length=255, null=True, blank=True)
    api_endpoint = models.CharField(max_length=255, null=True, blank=True)
    custom_base_url = models.BooleanField(default=False, null=True, blank=True)
    api_endpoint_args = models.CharField(max_length=255, null=True, blank=True)
    auth_url_data = models.CharField(max_length=255, null=True, blank=True)
    user_id_property = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_SIGN_UPS = [
        ("Allow", "Allow"),
        ("Deny", "Deny"),
    ]
    sign_ups = models.CharField(choices=CHOICES_SIGN_UPS, max_length=255, null=True, blank=True)
