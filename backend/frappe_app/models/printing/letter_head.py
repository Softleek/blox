from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class LetterHead(BaseModel):
    letter_head_name = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_SOURCE = [
        ("Image", "Image"),
        ("HTML", "HTML"),
    ]
    source = models.CharField(choices=CHOICES_SOURCE, max_length=255, null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    is_default = models.BooleanField(default=False, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    CHOICES_ALIGN = [
        ("Left", "Left"),
        ("Right", "Right"),
        ("Center", "Center"),
    ]
    align = models.CharField(choices=CHOICES_ALIGN, max_length=255, default='Left', null=True, blank=True)
    image_height = models.FloatField(null=True, blank=True)
    image_width = models.FloatField(null=True, blank=True)
    footer_image = models.CharField(max_length=255, null=True, blank=True)
    footer_image_height = models.FloatField(null=True, blank=True)
    footer_image_width = models.FloatField(null=True, blank=True)
    CHOICES_FOOTER_ALIGN = [
        ("Left", "Left"),
        ("Right", "Right"),
        ("Center", "Center"),
    ]
    footer_align = models.CharField(choices=CHOICES_FOOTER_ALIGN, max_length=255, null=True, blank=True)
    CHOICES_FOOTER_SOURCE = [
        ("Image", "Image"),
        ("HTML", "HTML"),
    ]
    footer_source = models.CharField(choices=CHOICES_FOOTER_SOURCE, max_length=255, default='HTML', null=True, blank=True)
    header_script = models.CharField(max_length=255, null=True, blank=True)
    footer_script = models.CharField(max_length=255, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
