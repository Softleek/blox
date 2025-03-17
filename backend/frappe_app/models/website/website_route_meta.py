from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebsiteRouteMeta(BaseModel):
    meta_tags = models.ManyToManyField("frappe_app.WebsiteMetaTag", related_name="WebsiteRouteMetaMetaTags", )
