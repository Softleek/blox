from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class GlobalSearchSettings(SingletonModel):
    allowed_in_global_search = models.ManyToManyField("frappe_app.GlobalSearchDoctype", related_name="GlobalSearchSettingsAllowedInGlobalSearch", )
