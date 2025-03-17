from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Page(BaseModel):
    system_page = models.BooleanField(default=False, null=True, blank=True)
    page_name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="PageModule", on_delete=models.CASCADE, null=True, blank=True)
    restrict_to_domain = models.ForeignKey("frappe_app.Domain", related_name="PageRestrictToDomain", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_STANDARD = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]
    standard = models.CharField(choices=CHOICES_STANDARD, max_length=255, null=True, blank=True)
    roles = models.ManyToManyField("frappe_app.HasRole", related_name="PageRoles", )
