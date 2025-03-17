from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class HelpArticle(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey("frappe_app.HelpCategory", related_name="HelpArticleCategory", on_delete=models.CASCADE, null=True, blank=True)
    published = models.BooleanField(default=False, null=True, blank=True)
    author = models.CharField(max_length=255, default='user_fullname', null=True, blank=True)
    CHOICES_LEVEL = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Expert", "Expert"),
    ]
    level = models.CharField(choices=CHOICES_LEVEL, max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    helpful = models.IntegerField(default=0, null=True, blank=True)
    not_helpful = models.IntegerField(default=0, null=True, blank=True)
