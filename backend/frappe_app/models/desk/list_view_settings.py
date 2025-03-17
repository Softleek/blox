from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ListViewSettings(BaseModel):
    disable_count = models.BooleanField(default=False, null=True, blank=True)
    disable_sidebar_stats = models.BooleanField(default=False, null=True, blank=True)
    disable_auto_refresh = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_TOTAL_FIELDS = [
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    ]
    total_fields = models.CharField(choices=CHOICES_TOTAL_FIELDS, max_length=255, null=True, blank=True)
    fields_html = models.TextField(null=True, blank=True)
    fields = models.CharField(max_length=255, null=True, blank=True)
    disable_comment_count = models.BooleanField(default=False, null=True, blank=True)
    allow_edit = models.BooleanField(default=False, null=True, blank=True)
    disable_automatic_recency_filters = models.BooleanField(default=False, null=True, blank=True)
