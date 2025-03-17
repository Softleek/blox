from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ContactUsSettings(SingletonModel):
    forward_to_email = models.CharField(max_length=255, null=True, blank=True)
    heading = models.CharField(max_length=255, null=True, blank=True)
    introduction = models.CharField(max_length=255, null=True, blank=True)
    query_options = models.TextField(null=True, blank=True)
    address_title = models.CharField(max_length=255, null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email_id = models.CharField(max_length=255, null=True, blank=True)
    skype = models.CharField(max_length=255, null=True, blank=True)
    disable_contact_us = models.BooleanField(default=False, null=True, blank=True)
