from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class NetworkPrinterSettings(BaseModel):
    server_ip = models.CharField(max_length=255, default='localhost', null=True, blank=True)
    port = models.IntegerField(default=631, null=True, blank=True)
    CHOICES_PRINTER_NAME = [
        ("", ""),
    ]
    printer_name = models.CharField(choices=CHOICES_PRINTER_NAME, max_length=255, null=True, blank=True)
