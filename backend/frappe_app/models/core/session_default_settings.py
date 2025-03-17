from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SessionDefaultSettings(SingletonModel):
    session_defaults = models.ManyToManyField("frappe_app.SessionDefault", related_name="SessionDefaultSettingsSessionDefaults", )
