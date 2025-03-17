from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class BlogPost(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    published_on = models.DateField(null=True, blank=True)
    published = models.BooleanField(default=False, null=True, blank=True)
    blog_category = models.ForeignKey("frappe_app.BlogCategory", related_name="BlogPostBlogCategory", on_delete=models.CASCADE, null=True, blank=True)
    blogger = models.ForeignKey("frappe_app.Blogger", related_name="BlogPostBlogger", on_delete=models.CASCADE, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    blog_intro = models.TextField(null=True, blank=True)
    CHOICES_CONTENT_TYPE = [
        ("Markdown", "Markdown"),
        ("Rich Text", "Rich Text"),
        ("HTML", "HTML"),
    ]
    content_type = models.CharField(choices=CHOICES_CONTENT_TYPE, max_length=255, default='Markdown', null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    content_md = models.TextField(null=True, blank=True)
    content_html = models.TextField(null=True, blank=True)
    email_sent = models.BooleanField(default=False, null=True, blank=True)
    disable_comments = models.BooleanField(default=False, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_image = models.CharField(max_length=255, null=True, blank=True)
    google_preview = models.TextField(null=True, blank=True)
    read_time = models.IntegerField(null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)
    hide_cta = models.BooleanField(default=False, null=True, blank=True)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    enable_email_notification = models.BooleanField(default=True, null=True, blank=True)
    disable_likes = models.BooleanField(default=False, null=True, blank=True)
