from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DomainSettings(SingletonModel):
    domains_html = models.TextField(null=True, blank=True)
    active_domains = models.ManyToManyField("frappe_app.HasDomain", related_name="DomainSettingsActiveDomains", )
