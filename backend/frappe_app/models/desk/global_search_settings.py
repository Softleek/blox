from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import SingletonModel

class GlobalSearchSettings(SingletonModel):
    allowed_in_global_search = models.ManyToManyField("frappe_app.GlobalSearchDoctype", related_name="GlobalSearchSettingsAllowedInGlobalSearch", )
