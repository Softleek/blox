from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DocumentNamingRule(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="DocumentNamingRuleDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    prefix = models.CharField(max_length=255, null=True, blank=True)
    counter = models.IntegerField(default=0, null=True, blank=True)
    prefix_digits = models.IntegerField(default=5, null=True, blank=True)
    conditions = models.ManyToManyField("frappe_app.DocumentNamingRuleCondition", related_name="DocumentNamingRuleConditions", )
    priority = models.IntegerField(null=True, blank=True)
