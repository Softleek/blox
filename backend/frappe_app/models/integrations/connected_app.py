from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ConnectedApp(BaseModel):
    provider_name = models.CharField(max_length=255, null=True, blank=True)
    openid_configuration = models.CharField(max_length=255, null=True, blank=True)
    client_id = models.CharField(max_length=255, null=True, blank=True)
    redirect_uri = models.CharField(max_length=255, null=True, blank=True)
    client_secret = models.CharField(max_length=255, null=True, blank=True)
    scopes = models.ManyToManyField("frappe_app.OauthScope", related_name="ConnectedAppScopes", )
    authorization_uri = models.TextField(null=True, blank=True)
    token_uri = models.CharField(max_length=255, null=True, blank=True)
    revocation_uri = models.CharField(max_length=255, null=True, blank=True)
    userinfo_uri = models.CharField(max_length=255, null=True, blank=True)
    introspection_uri = models.CharField(max_length=255, null=True, blank=True)
    query_parameters = models.ManyToManyField("frappe_app.QueryParameters", related_name="ConnectedAppQueryParameters", )
