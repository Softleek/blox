from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import SingletonModel

class InstalledApplications(SingletonModel):
    installed_applications = models.ManyToManyField("frappe_app.InstalledApplication", related_name="InstalledApplicationsInstalledApplications", )
