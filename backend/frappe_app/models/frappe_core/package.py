from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Package(BaseModel):
    readme = models.TextField(null=True, blank=True)
    package_name = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_LICENSE_TYPE = [
        ("MIT License", "MIT License"),
        ("GNU General Public License", "GNU General Public License"),
        ("GNU Affero General Public License", "GNU Affero General Public License"),
    ]
    license_type = models.CharField(choices=CHOICES_LICENSE_TYPE, max_length=255, null=True, blank=True)
    license = models.TextField(null=True, blank=True)
