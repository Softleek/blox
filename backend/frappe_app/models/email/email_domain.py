from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EmailDomain(BaseModel):
    domain_name = models.CharField(max_length=255, null=True, blank=True)
    email_server = models.CharField(max_length=255, null=True, blank=True)
    use_imap = models.BooleanField(default=False, null=True, blank=True)
    use_ssl = models.BooleanField(default=False, null=True, blank=True)
    use_starttls = models.BooleanField(default=False, null=True, blank=True)
    attachment_limit = models.IntegerField(null=True, blank=True)
    smtp_server = models.CharField(max_length=255, null=True, blank=True)
    use_tls = models.BooleanField(default=False, null=True, blank=True)
    smtp_port = models.CharField(max_length=255, null=True, blank=True)
    incoming_port = models.CharField(max_length=255, null=True, blank=True)
    append_emails_to_sent_folder = models.BooleanField(default=False, null=True, blank=True)
    use_ssl_for_outgoing = models.BooleanField(default=False, null=True, blank=True)
    validate_ssl_certificate = models.BooleanField(default=True, null=True, blank=True)
    validate_ssl_certificate_for_outgoing = models.BooleanField(default=True, null=True, blank=True)
    sent_folder_name = models.CharField(max_length=255, default='Sent', null=True, blank=True)
