from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class SMSLog(BaseModel):
    sender_name = models.CharField(max_length=255, null=True, blank=True)
    sent_on = models.DateField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    no_of_requested_sms = models.IntegerField(null=True, blank=True)
    requested_numbers = models.CharField(max_length=255, null=True, blank=True)
    no_of_sent_sms = models.IntegerField(null=True, blank=True)
    sent_to = models.CharField(max_length=255, null=True, blank=True)
