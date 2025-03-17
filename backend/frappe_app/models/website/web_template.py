from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebTemplate(BaseModel):
    template = models.CharField(max_length=255, null=True, blank=True)
    fields = models.ManyToManyField("frappe_app.WebTemplateField", related_name="WebTemplateFields", )
    standard = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_TYPE = [
        ("Component", "Component"),
        ("Section", "Section"),
        ("Navbar", "Navbar"),
        ("Footer", "Footer"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, default='Section', null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="WebTemplateModule", on_delete=models.CASCADE, null=True, blank=True)
