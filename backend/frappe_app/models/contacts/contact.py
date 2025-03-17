from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Contact(BaseModel):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email_id = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="ContactUser", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_STATUS = [
        ("Passive", "Passive"),
        ("Open", "Open"),
        ("Replied", "Replied"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Passive', null=True, blank=True)
    salutation = models.ForeignKey("frappe_app.Salutation", related_name="ContactSalutation", on_delete=models.CASCADE, null=True, blank=True)
    gender = models.ForeignKey("frappe_app.Gender", related_name="ContactGender", on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    is_primary_contact = models.BooleanField(default=False, null=True, blank=True)
    links = models.ManyToManyField("frappe_app.DynamicLink", related_name="ContactLinks", )
    department = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    unsubscribed = models.BooleanField(default=False, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    email_ids = models.ManyToManyField("frappe_app.ContactEmail", related_name="ContactEmailIds", )
    address = models.ForeignKey("frappe_app.Address", related_name="ContactAddress", on_delete=models.CASCADE, null=True, blank=True)
    phone_nos = models.ManyToManyField("frappe_app.ContactPhone", related_name="ContactPhoneNos", )
    mobile_no = models.CharField(max_length=255, null=True, blank=True)
    pulled_from_google_contacts = models.BooleanField(default=False, null=True, blank=True)
    sync_with_google_contacts = models.BooleanField(default=False, null=True, blank=True)
    google_contacts = models.ForeignKey("frappe_app.GoogleContacts", related_name="ContactGoogleContacts", on_delete=models.CASCADE, null=True, blank=True)
    custom_google_contacts = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
