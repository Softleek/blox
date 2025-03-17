from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EnergyPointRule(BaseModel):
    enabled = models.BooleanField(default=True, null=True, blank=True)
    rule_name = models.CharField(max_length=255, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="EnergyPointRuleReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    condition = models.CharField(max_length=255, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    CHOICES_USER_FIELD = [
        ("", ""),
    ]
    user_field = models.CharField(choices=CHOICES_USER_FIELD, max_length=255, null=True, blank=True)
    CHOICES_MULTIPLIER_FIELD = [
        ("", ""),
    ]
    multiplier_field = models.CharField(choices=CHOICES_MULTIPLIER_FIELD, max_length=255, null=True, blank=True)
    max_points = models.IntegerField(null=True, blank=True)
    CHOICES_FOR_DOC_EVENT = [
        ("New", "New"),
        ("Submit", "Submit"),
        ("Cancel", "Cancel"),
        ("Value Change", "Value Change"),
        ("Custom", "Custom"),
    ]
    for_doc_event = models.CharField(choices=CHOICES_FOR_DOC_EVENT, max_length=255, default='Custom', null=True, blank=True)
    for_assigned_users = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_FIELD_TO_CHECK = [
        ("", ""),
    ]
    field_to_check = models.CharField(choices=CHOICES_FIELD_TO_CHECK, max_length=255, null=True, blank=True)
    apply_only_once = models.BooleanField(default=False, null=True, blank=True)
