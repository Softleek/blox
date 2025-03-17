from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Communication(BaseModel):
    subject = models.TextField(null=True, blank=True)
    CHOICES_COMMUNICATION_MEDIUM = [
        ("Email", "Email"),
        ("Chat", "Chat"),
        ("Phone", "Phone"),
        ("SMS", "SMS"),
        ("Event", "Event"),
        ("Meeting", "Meeting"),
        ("Visit", "Visit"),
        ("Other", "Other"),
    ]
    communication_medium = models.CharField(choices=CHOICES_COMMUNICATION_MEDIUM, max_length=255, null=True, blank=True)
    sender = models.CharField(max_length=255, null=True, blank=True)
    recipients = models.CharField(max_length=255, null=True, blank=True)
    cc = models.CharField(max_length=255, null=True, blank=True)
    bcc = models.CharField(max_length=255, null=True, blank=True)
    phone_no = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_DELIVERY_STATUS = [
        ("Sent", "Sent"),
        ("Bounced", "Bounced"),
        ("Opened", "Opened"),
        ("Marked As Spam", "Marked As Spam"),
        ("Rejected", "Rejected"),
        ("Delayed", "Delayed"),
        ("Soft-Bounced", "Soft-Bounced"),
        ("Clicked", "Clicked"),
        ("Recipient Unsubscribed", "Recipient Unsubscribed"),
        ("Error", "Error"),
        ("Expired", "Expired"),
        ("Sending", "Sending"),
        ("Read", "Read"),
        ("Scheduled", "Scheduled"),
    ]
    delivery_status = models.CharField(choices=CHOICES_DELIVERY_STATUS, max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    text_content = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_COMMUNICATION_TYPE = [
        ("Communication", "Communication"),
        ("Automated Message", "Automated Message"),
    ]
    communication_type = models.CharField(choices=CHOICES_COMMUNICATION_TYPE, max_length=255, default='Communication', null=True, blank=True)
    CHOICES_STATUS = [
        ("Open", "Open"),
        ("Replied", "Replied"),
        ("Closed", "Closed"),
        ("Linked", "Linked"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
    CHOICES_SENT_OR_RECEIVED = [
        ("Sent", "Sent"),
        ("Received", "Received"),
    ]
    sent_or_received = models.CharField(choices=CHOICES_SENT_OR_RECEIVED, max_length=255, null=True, blank=True)
    communication_date = models.DateTimeField(default='Now', null=True, blank=True)
    read_receipt = models.BooleanField(default=False, null=True, blank=True)
    sender_full_name = models.CharField(max_length=255, null=True, blank=True)
    read_by_recipient = models.BooleanField(default=False, null=True, blank=True)
    read_by_recipient_on = models.DateTimeField(null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="CommunicationReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    reference_owner = models.CharField(max_length=255, null=True, blank=True)
    email_account = models.ForeignKey("frappe_app.EmailAccount", related_name="CommunicationEmailAccount", on_delete=models.CASCADE, null=True, blank=True)
    in_reply_to = models.ForeignKey("frappe_app.Communication", related_name="CommunicationInReplyTo", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="CommunicationUser", on_delete=models.CASCADE, default='__user', null=True, blank=True)
    unread_notification_sent = models.BooleanField(default=False, null=True, blank=True)
    seen = models.BooleanField(default=False, null=True, blank=True)
    _user_tags = models.CharField(max_length=255, null=True, blank=True)
    message_id = models.TextField(null=True, blank=True)
    uid = models.IntegerField(null=True, blank=True)
    CHOICES_EMAIL_STATUS = [
        ("Open", "Open"),
        ("Spam", "Spam"),
        ("Trash", "Trash"),
    ]
    email_status = models.CharField(choices=CHOICES_EMAIL_STATUS, max_length=255, null=True, blank=True)
    has_attachment = models.BooleanField(default=False, null=True, blank=True)
    email_template = models.ForeignKey("frappe_app.EmailTemplate", related_name="CommunicationEmailTemplate", on_delete=models.CASCADE, null=True, blank=True)
    timeline_links = models.ManyToManyField("frappe_app.CommunicationLink", related_name="CommunicationTimelineLinks", )
    imap_folder = models.CharField(max_length=255, null=True, blank=True)
    send_after = models.DateTimeField(null=True, blank=True)
