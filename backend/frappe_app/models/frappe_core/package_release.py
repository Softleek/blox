from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PackageRelease(BaseModel):
    package = models.ForeignKey("frappe_app.Package", related_name="PackageReleasePackage", on_delete=models.CASCADE, null=True, blank=True)
    major = models.IntegerField(null=True, blank=True)
    minor = models.IntegerField(null=True, blank=True)
    patch = models.IntegerField(null=True, blank=True)
    path = models.TextField(null=True, blank=True)
    release_notes = models.TextField(null=True, blank=True)
    publish = models.BooleanField(default=False, null=True, blank=True)
