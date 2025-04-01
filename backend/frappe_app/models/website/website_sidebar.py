from django.db import models
from multiselectfield import MultiSelectField
from datetime import timedelta
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class WebsiteSidebar(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    sidebar_items = models.ManyToManyField("frappe_app.WebsiteSidebarItem", related_name="WebsiteSidebarSidebarItems", )
