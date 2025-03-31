from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class DocumentNamingRuleCondition(BaseModel):
    CHOICES_FIELD = [
        ("", ""),
    ]
    field = models.CharField(choices=CHOICES_FIELD, max_length=255, null=True, blank=True)
    CHOICES_CONDITION = [
        ("=", "="),
        ("!=", "!="),
        (">", ">"),
        ("<", "<"),
        (">=", ">="),
        ("<=", "<="),
    ]
    condition = models.CharField(choices=CHOICES_CONDITION, max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
