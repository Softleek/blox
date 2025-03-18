from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class LogSettings(SingletonModel):
    logs_to_clear = models.ManyToManyField("frappe_app.LogsToClear", related_name="LogSettingsLogsToClear", )
