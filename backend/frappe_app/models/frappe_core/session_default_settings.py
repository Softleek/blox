from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import SingletonModel

class SessionDefaultSettings(SingletonModel):
    session_defaults = models.ManyToManyField("frappe_app.SessionDefault", related_name="SessionDefaultSettingsSessionDefaults", )
