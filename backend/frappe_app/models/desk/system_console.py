from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SystemConsole(SingletonModel):
    console = models.CharField(max_length=255, null=True, blank=True)
    output = models.CharField(max_length=255, null=True, blank=True)
    commit = models.BooleanField(default=False, null=True, blank=True)
    show_processlist = models.BooleanField(default=False, null=True, blank=True)
    processlist = models.TextField(null=True, blank=True)
    CHOICES_TYPE = [
        ("Python", "Python"),
        ("SQL", "SQL"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, default='Python', null=True, blank=True)
    sql_output = models.TextField(null=True, blank=True)
