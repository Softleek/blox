from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Address(BaseModel):
    address_title = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_ADDRESS_TYPE = [
        ("Billing", "Billing"),
        ("Shipping", "Shipping"),
        ("Office", "Office"),
        ("Personal", "Personal"),
        ("Plant", "Plant"),
        ("Postal", "Postal"),
        ("Shop", "Shop"),
        ("Subsidiary", "Subsidiary"),
        ("Warehouse", "Warehouse"),
        ("Current", "Current"),
        ("Permanent", "Permanent"),
        ("Other", "Other"),
    ]
    address_type = models.CharField(choices=CHOICES_ADDRESS_TYPE, max_length=255, null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey("frappe_app.Country", related_name="AddressCountry", on_delete=models.CASCADE, null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    email_id = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    is_primary_address = models.BooleanField(default=False, null=True, blank=True)
    is_shipping_address = models.BooleanField(default=False, null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    links = models.ManyToManyField("frappe_app.DynamicLink", related_name="AddressLinks", )
