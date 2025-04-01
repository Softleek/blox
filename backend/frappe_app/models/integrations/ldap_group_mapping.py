from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class LDAPGroupMapping(BaseModel):
    ldap_group = models.CharField(max_length=255, null=True, blank=True)
    erpnext_role = models.ForeignKey("frappe_app.Role", related_name="LDAPGroupMappingErpnextRole", on_delete=models.CASCADE, null=True, blank=True)
