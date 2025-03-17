from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EmailGroup(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    total_subscribers = models.IntegerField(default=0, null=True, blank=True)
    confirmation_email_template = models.ForeignKey("frappe_app.EmailTemplate", related_name="EmailGroupConfirmationEmailTemplate", on_delete=models.CASCADE, null=True, blank=True)
    welcome_email_template = models.ForeignKey("frappe_app.EmailTemplate", related_name="EmailGroupWelcomeEmailTemplate", on_delete=models.CASCADE, null=True, blank=True)
    welcome_url = models.CharField(max_length=255, null=True, blank=True)
    add_query_parameters = models.BooleanField(default=False, null=True, blank=True)
