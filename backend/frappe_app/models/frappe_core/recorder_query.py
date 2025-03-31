from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class RecorderQuery(BaseModel):
    query = models.CharField(max_length=255, null=True, blank=True)
    normalized_query = models.CharField(max_length=255, null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    exact_copies = models.IntegerField(null=True, blank=True)
    normalized_copies = models.IntegerField(null=True, blank=True)
    stack = models.TextField(null=True, blank=True)
    stack_html = models.TextField(null=True, blank=True)
    explain_result = models.TextField(null=True, blank=True)
    sql_explain_html = models.TextField(null=True, blank=True)
    index = models.IntegerField(null=True, blank=True)
