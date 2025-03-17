from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EmailAccount(BaseModel):
    email_id = models.CharField(max_length=255, null=True, blank=True)
    login_id_is_different = models.BooleanField(default=False, null=True, blank=True)
    login_id = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    awaiting_password = models.BooleanField(default=False, null=True, blank=True)
    ascii_encode_password = models.BooleanField(default=False, null=True, blank=True)
    email_account_name = models.CharField(max_length=255, null=True, blank=True)
    domain = models.ForeignKey("frappe_app.EmailDomain", related_name="EmailAccountDomain", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_SERVICE = [
        ("Frappe Mail", "Frappe Mail"),
        ("GMail", "GMail"),
        ("Sendgrid", "Sendgrid"),
        ("SparkPost", "SparkPost"),
        ("Yahoo Mail", "Yahoo Mail"),
        ("Outlook.com", "Outlook.com"),
        ("Yandex.Mail", "Yandex.Mail"),
    ]
    service = models.CharField(choices=CHOICES_SERVICE, max_length=255, null=True, blank=True)
    enable_incoming = models.BooleanField(default=False, null=True, blank=True)
    use_imap = models.BooleanField(default=False, null=True, blank=True)
    email_server = models.CharField(max_length=255, null=True, blank=True)
    use_ssl = models.BooleanField(default=False, null=True, blank=True)
    attachment_limit = models.IntegerField(null=True, blank=True)
    append_to = models.ForeignKey("frappe_app.Doctype", related_name="EmailAccountAppendTo", on_delete=models.CASCADE, null=True, blank=True)
    default_incoming = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_EMAIL_SYNC_OPTION = [
        ("ALL", "ALL"),
        ("UNSEEN", "UNSEEN"),
    ]
    email_sync_option = models.CharField(choices=CHOICES_EMAIL_SYNC_OPTION, max_length=255, default='UNSEEN', null=True, blank=True)
    CHOICES_INITIAL_SYNC_COUNT = [
        ("100", "100"),
        ("250", "250"),
        ("500", "500"),
    ]
    initial_sync_count = models.CharField(choices=CHOICES_INITIAL_SYNC_COUNT, max_length=255, default='250', null=True, blank=True)
    notify_if_unreplied = models.BooleanField(default=False, null=True, blank=True)
    unreplied_for_mins = models.IntegerField(default=30, null=True, blank=True)
    send_notification_to = models.TextField(null=True, blank=True)
    enable_outgoing = models.BooleanField(default=False, null=True, blank=True)
    smtp_server = models.CharField(max_length=255, null=True, blank=True)
    use_tls = models.BooleanField(default=False, null=True, blank=True)
    smtp_port = models.CharField(max_length=255, null=True, blank=True)
    default_outgoing = models.BooleanField(default=False, null=True, blank=True)
    always_use_account_email_id_as_sender = models.BooleanField(default=False, null=True, blank=True)
    always_use_account_name_as_sender_name = models.BooleanField(default=False, null=True, blank=True)
    send_unsubscribe_message = models.BooleanField(default=True, null=True, blank=True)
    track_email_status = models.BooleanField(default=True, null=True, blank=True)
    no_smtp_authentication = models.BooleanField(default=False, null=True, blank=True)
    add_signature = models.BooleanField(default=False, null=True, blank=True)
    signature = models.CharField(max_length=255, null=True, blank=True)
    enable_auto_reply = models.BooleanField(default=False, null=True, blank=True)
    auto_reply_message = models.CharField(max_length=255, null=True, blank=True)
    footer = models.CharField(max_length=255, null=True, blank=True)
    uidvalidity = models.CharField(max_length=255, null=True, blank=True)
    uidnext = models.IntegerField(null=True, blank=True)
    no_failed = models.IntegerField(null=True, blank=True)
    enable_automatic_linking = models.BooleanField(default=False, null=True, blank=True)
    incoming_port = models.CharField(max_length=255, null=True, blank=True)
    append_emails_to_sent_folder = models.BooleanField(default=False, null=True, blank=True)
    use_ssl_for_outgoing = models.BooleanField(default=False, null=True, blank=True)
    create_contact = models.BooleanField(default=True, null=True, blank=True)
    brand_logo = models.CharField(max_length=255, null=True, blank=True)
    imap_folder = models.ManyToManyField("frappe_app.ImapFolder", related_name="EmailAccountImapFolder", )
    authorize_api_access = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_AUTH_METHOD = [
        ("Basic", "Basic"),
        ("OAuth", "OAuth"),
    ]
    auth_method = models.CharField(choices=CHOICES_AUTH_METHOD, max_length=255, default='Basic', null=True, blank=True)
    use_starttls = models.BooleanField(default=False, null=True, blank=True)
    connected_app = models.ForeignKey("frappe_app.ConnectedApp", related_name="EmailAccountConnectedApp", on_delete=models.CASCADE, null=True, blank=True)
    connected_user = models.ForeignKey("frappe_app.User", related_name="EmailAccountConnectedUser", on_delete=models.CASCADE, null=True, blank=True)
    validate_ssl_certificate = models.BooleanField(default=True, null=True, blank=True)
    frappe_mail_site = models.CharField(max_length=255, default='https://frappemail.com', null=True, blank=True)
    last_synced_at = models.DateTimeField(null=True, blank=True)
    validate_frappe_mail_settings = models.CharField(max_length=255, null=True, blank=True)
    api_key = models.CharField(max_length=255, null=True, blank=True)
    api_secret = models.CharField(max_length=255, null=True, blank=True)
    backend_app_flow = models.BooleanField(default=False, null=True, blank=True)
    sent_folder_name = models.CharField(max_length=255, null=True, blank=True)
    always_bcc = models.CharField(max_length=255, null=True, blank=True)
