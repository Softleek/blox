from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Comment(BaseModel):
    CHOICES_COMMENT_TYPE = [
        ("Comment", "Comment"),
        ("Like", "Like"),
        ("Info", "Info"),
        ("Label", "Label"),
        ("Workflow", "Workflow"),
        ("Created", "Created"),
        ("Submitted", "Submitted"),
        ("Cancelled", "Cancelled"),
        ("Updated", "Updated"),
        ("Deleted", "Deleted"),
        ("Assigned", "Assigned"),
        ("Assignment Completed", "Assignment Completed"),
        ("Attachment", "Attachment"),
        ("Attachment Removed", "Attachment Removed"),
        ("Shared", "Shared"),
        ("Unshared", "Unshared"),
        ("Bot", "Bot"),
        ("Relinked", "Relinked"),
        ("Edit", "Edit"),
    ]
    comment_type = models.CharField(choices=CHOICES_COMMENT_TYPE, max_length=255, default='Comment', null=True, blank=True)
    comment_email = models.CharField(max_length=255, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    comment_by = models.CharField(max_length=255, null=True, blank=True)
    published = models.BooleanField(default=False, null=True, blank=True)
    seen = models.BooleanField(default=False, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="CommentReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    reference_owner = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
