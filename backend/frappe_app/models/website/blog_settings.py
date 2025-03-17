from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class BlogSettings(SingletonModel):
    blog_title = models.CharField(max_length=255, null=True, blank=True)
    blog_introduction = models.TextField(null=True, blank=True)
    enable_social_sharing = models.BooleanField(default=False, null=True, blank=True)
    show_cta_in_blog = models.BooleanField(default=False, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    cta_label = models.CharField(max_length=255, null=True, blank=True)
    cta_url = models.CharField(max_length=255, null=True, blank=True)
    comment_limit = models.IntegerField(default=5, null=True, blank=True)
    allow_guest_to_comment = models.BooleanField(default=True, null=True, blank=True)
    browse_by_category = models.BooleanField(default=False, null=True, blank=True)
    like_limit = models.IntegerField(default=5, null=True, blank=True)
    preview_image = models.CharField(max_length=255, null=True, blank=True)
