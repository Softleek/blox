from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import SingletonModel

class RoleReplication(SingletonModel):
    existing_role = models.ForeignKey("frappe_app.Role", related_name="RoleReplicationExistingRole", on_delete=models.CASCADE, null=True, blank=True)
    new_role = models.CharField(max_length=255, null=True, blank=True)
