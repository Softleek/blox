from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class InstalledApplications(SingletonModel):
    installed_applications = models.ManyToManyField("frappe_app.InstalledApplication", related_name="InstalledApplicationsInstalledApplications", )
