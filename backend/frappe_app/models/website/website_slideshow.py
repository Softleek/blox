from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class WebsiteSlideshow(BaseModel):
    slideshow_name = models.CharField(max_length=255, null=True, blank=True)
    slideshow_items = models.ManyToManyField("frappe_app.WebsiteSlideshowItem", related_name="WebsiteSlideshowSlideshowItems", )
    header = models.TextField(null=True, blank=True)
