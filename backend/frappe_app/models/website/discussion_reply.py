from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class DiscussionReply(BaseModel):
    reply = models.CharField(max_length=255, null=True, blank=True)
    topic = models.ForeignKey("frappe_app.DiscussionTopic", related_name="DiscussionReplyTopic", on_delete=models.CASCADE, null=True, blank=True)
