from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SuccessAction(BaseModel):
    ref_doctype = models.ForeignKey("frappe_app.Doctype", related_name="SuccessActionRefDoctype", on_delete=models.CASCADE, null=True, blank=True)
    first_success_message = models.CharField(max_length=255, default='Congratulations on first creations', null=True, blank=True)
    message = models.CharField(max_length=255, default='Successfully created', null=True, blank=True)
    next_actions_html = models.TextField(null=True, blank=True)
    next_actions = models.CharField(max_length=255, null=True, blank=True)
    action_timeout = models.IntegerField(default=7, null=True, blank=True)
