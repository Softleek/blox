from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkspaceSettings(SingletonModel):
    workspace_visibility_json = models.JSONField(null=True, blank=True)
    workspace_setup_completed = models.BooleanField(default=False, null=True, blank=True)
