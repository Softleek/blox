from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Recorder(BaseModel):
    path = models.CharField(max_length=255, null=True, blank=True)
    cmd = models.CharField(max_length=255, null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    number_of_queries = models.IntegerField(null=True, blank=True)
    time_in_queries = models.FloatField(null=True, blank=True)
    request_headers = models.CharField(max_length=255, null=True, blank=True)
    form_dict = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_METHOD = [
        ("GET", "GET"),
        ("POST", "POST"),
        ("PUT", "PUT"),
        ("DELETE", "DELETE"),
        ("PATCH", "PATCH"),
        ("HEAD", "HEAD"),
        ("OPTIONS", "OPTIONS"),
    ]
    method = models.CharField(choices=CHOICES_METHOD, max_length=255, null=True, blank=True)
    sql_queries = models.ManyToManyField("frappe_app.RecorderQuery", related_name="RecorderSqlQueries", )
    event_type = models.CharField(max_length=255, null=True, blank=True)
    profile = models.CharField(max_length=255, null=True, blank=True)
    suggested_indexes = models.ManyToManyField("frappe_app.RecorderSuggestedIndex", related_name="RecorderSuggestedIndexes", )
