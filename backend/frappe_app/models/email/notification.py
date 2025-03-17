from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Notification(BaseModel):
    enabled = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_CHANNEL = [
        ("Email", "Email"),
        ("Slack", "Slack"),
        ("System Notification", "System Notification"),
        ("SMS", "SMS"),
    ]
    channel = models.CharField(choices=CHOICES_CHANNEL, max_length=255, default='Email', null=True, blank=True)
    slack_webhook_url = models.ForeignKey("frappe_app.SlackWebhookUrl", related_name="NotificationSlackWebhookUrl", on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="NotificationDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    is_standard = models.BooleanField(default=False, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="NotificationModule", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_EVENT = [
        ("New", "New"),
        ("Save", "Save"),
        ("Submit", "Submit"),
        ("Cancel", "Cancel"),
        ("Days After", "Days After"),
        ("Days Before", "Days Before"),
        ("Minutes After", "Minutes After"),
        ("Minutes Before", "Minutes Before"),
        ("Value Change", "Value Change"),
        ("Method", "Method"),
        ("Custom", "Custom"),
    ]
    event = models.CharField(choices=CHOICES_EVENT, max_length=255, null=True, blank=True)
    method = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_DATE_CHANGED = [
        ("", ""),
    ]
    date_changed = models.CharField(choices=CHOICES_DATE_CHANGED, max_length=255, null=True, blank=True)
    days_in_advance = models.IntegerField(default=0, null=True, blank=True)
    CHOICES_VALUE_CHANGED = [
        ("", ""),
    ]
    value_changed = models.CharField(choices=CHOICES_VALUE_CHANGED, max_length=255, null=True, blank=True)
    sender = models.ForeignKey("frappe_app.EmailAccount", related_name="NotificationSender", on_delete=models.CASCADE, null=True, blank=True)
    sender_email = models.CharField(max_length=255, null=True, blank=True)
    condition = models.CharField(max_length=255, null=True, blank=True)
    html_7 = models.TextField(null=True, blank=True)
    CHOICES_SET_PROPERTY_AFTER_ALERT = [
        ("", ""),
    ]
    set_property_after_alert = models.CharField(choices=CHOICES_SET_PROPERTY_AFTER_ALERT, max_length=255, null=True, blank=True)
    property_value = models.CharField(max_length=255, null=True, blank=True)
    recipients = models.ManyToManyField("frappe_app.NotificationRecipient", related_name="NotificationRecipients", )
    message = models.CharField(max_length=255, default='Add your message here', null=True, blank=True)
    message_examples = models.TextField(null=True, blank=True)
    view_properties = models.CharField(max_length=255, null=True, blank=True)
    attach_print = models.BooleanField(default=False, null=True, blank=True)
    print_format = models.ForeignKey("frappe_app.PrintFormat", related_name="NotificationPrintFormat", on_delete=models.CASCADE, null=True, blank=True)
    send_system_notification = models.BooleanField(default=False, null=True, blank=True)
    send_to_all_assignees = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_MESSAGE_TYPE = [
        ("Markdown", "Markdown"),
        ("HTML", "HTML"),
        ("Plain Text", "Plain Text"),
    ]
    message_type = models.CharField(choices=CHOICES_MESSAGE_TYPE, max_length=255, default='Markdown', null=True, blank=True)
    CHOICES_DATETIME_CHANGED = [
        ("", ""),
    ]
    datetime_changed = models.CharField(choices=CHOICES_DATETIME_CHANGED, max_length=255, null=True, blank=True)
    minutes_offset = models.IntegerField(default=0, null=True, blank=True)
    datetime_last_run = models.DateTimeField(null=True, blank=True)
