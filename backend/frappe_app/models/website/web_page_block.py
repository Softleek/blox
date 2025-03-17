from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebPageBlock(BaseModel):
    web_template = models.ForeignKey("frappe_app.WebTemplate", related_name="WebPageBlockWebTemplate", on_delete=models.CASCADE, null=True, blank=True)
    edit_values = models.CharField(max_length=255, null=True, blank=True)
    web_template_values = models.CharField(max_length=255, null=True, blank=True)
    css_class = models.TextField(null=True, blank=True)
    add_shade = models.BooleanField(default=False, null=True, blank=True)
    add_container = models.BooleanField(default=True, null=True, blank=True)
    hide_block = models.BooleanField(default=False, null=True, blank=True)
    add_top_padding = models.BooleanField(default=True, null=True, blank=True)
    add_bottom_padding = models.BooleanField(default=True, null=True, blank=True)
    add_border_at_top = models.BooleanField(default=False, null=True, blank=True)
    add_border_at_bottom = models.BooleanField(default=False, null=True, blank=True)
    add_background_image = models.BooleanField(default=False, null=True, blank=True)
    background_image = models.CharField(max_length=255, null=True, blank=True)
    section_id = models.CharField(max_length=255, null=True, blank=True)
