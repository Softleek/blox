from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PersonalDataDownloadRequest(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="PersonalDataDownloadRequestUser", on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    amended_from = models.ForeignKey("frappe_app.PersonalDataDownloadRequest", related_name="PersonalDataDownloadRequestAmendedFrom", on_delete=models.CASCADE, null=True, blank=True)
