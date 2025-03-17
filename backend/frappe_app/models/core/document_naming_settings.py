from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DocumentNamingSettings(SingletonModel):
    help_html = models.TextField(null=True, blank=True)
    user_must_always_select = models.BooleanField(default=False, null=True, blank=True)
    update = models.CharField(max_length=255, null=True, blank=True)
    prefix = models.CharField(max_length=255, null=True, blank=True)
    current_value = models.IntegerField(null=True, blank=True)
    update_series_start = models.CharField(max_length=255, null=True, blank=True)
    naming_series_options = models.TextField(null=True, blank=True)
    try_naming_series = models.CharField(max_length=255, null=True, blank=True)
    transaction_type = models.CharField(max_length=255, null=True, blank=True)
    series_preview = models.TextField(null=True, blank=True)
    CHOICES_DEFAULT_AMEND_NAMING = [
        ("Amend Counter", "Amend Counter"),
        ("Default Naming", "Default Naming"),
    ]
    default_amend_naming = models.CharField(choices=CHOICES_DEFAULT_AMEND_NAMING, max_length=255, default='Amend Counter', null=True, blank=True)
    amend_naming_override = models.ManyToManyField("frappe_app.AmendedDocumentNamingSettings", related_name="DocumentNamingSettingsAmendNamingOverride", )
    update_amendment_naming = models.CharField(max_length=255, null=True, blank=True)
