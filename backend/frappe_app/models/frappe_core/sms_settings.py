from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SMSSettings(SingletonModel):
    sms_gateway_url = models.TextField(null=True, blank=True)
    message_parameter = models.CharField(max_length=255, null=True, blank=True)
    receiver_parameter = models.CharField(max_length=255, null=True, blank=True)
    parameters = models.ManyToManyField("frappe_app.SmsParameter", related_name="SMSSettingsParameters", )
    use_post = models.BooleanField(default=False, null=True, blank=True)
