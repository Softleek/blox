from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class WebsiteRouteMeta(BaseModel):
    meta_tags = models.ManyToManyField("frappe_app.WebsiteMetaTag", related_name="WebsiteRouteMetaMetaTags", )
