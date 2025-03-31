from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import SingletonModel

class LogSettings(SingletonModel):
    logs_to_clear = models.ManyToManyField("frappe_app.LogsToClear", related_name="LogSettingsLogsToClear", )
