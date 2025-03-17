from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EmailQueue(BaseModel):
    sender = models.CharField(max_length=255, null=True, blank=True)
    recipients = models.ManyToManyField("frappe_app.EmailQueueRecipient", related_name="EmailQueueRecipients", )
    show_as_cc = models.TextField(null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Not Sent", "Not Sent"),
        ("Sending", "Sending"),
        ("Sent", "Sent"),
        ("Partially Sent", "Partially Sent"),
        ("Error", "Error"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Not Sent', null=True, blank=True)
    error = models.CharField(max_length=255, null=True, blank=True)
    custom_message = models.TextField(null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="EmailQueueReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    communication = models.ForeignKey("frappe_app.Communication", related_name="EmailQueueCommunication", on_delete=models.CASCADE, null=True, blank=True)
    send_after = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=1, null=True, blank=True)
    add_unsubscribe_link = models.BooleanField(default=True, null=True, blank=True)
    unsubscribe_method = models.CharField(max_length=255, null=True, blank=True)
    expose_recipients = models.CharField(max_length=255, null=True, blank=True)
    attachments = models.CharField(max_length=255, null=True, blank=True)
    retry = models.IntegerField(default=0, null=True, blank=True)
    email_account = models.ForeignKey("frappe_app.EmailAccount", related_name="EmailQueueEmailAccount", on_delete=models.CASCADE, null=True, blank=True)
    unsubscribe_params = models.CharField(max_length=255, null=True, blank=True)
