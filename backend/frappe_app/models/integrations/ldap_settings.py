from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class LDAPSettings(SingletonModel):
    enabled = models.BooleanField(default=False, null=True, blank=True)
    ldap_server_url = models.CharField(max_length=255, null=True, blank=True)
    base_dn = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    default_role = models.ForeignKey("frappe_app.Role", related_name="LDAPSettingsDefaultRole", on_delete=models.CASCADE, null=True, blank=True)
    ldap_search_string = models.CharField(max_length=255, null=True, blank=True)
    ldap_email_field = models.CharField(max_length=255, null=True, blank=True)
    ldap_username_field = models.CharField(max_length=255, null=True, blank=True)
    ldap_first_name_field = models.CharField(max_length=255, null=True, blank=True)
    ldap_middle_name_field = models.CharField(max_length=255, null=True, blank=True)
    ldap_last_name_field = models.CharField(max_length=255, null=True, blank=True)
    ldap_phone_field = models.CharField(max_length=255, null=True, blank=True)
    ldap_mobile_field = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_SSL_TLS_MODE = [
        ("Off", "Off"),
        ("StartTLS", "StartTLS"),
    ]
    ssl_tls_mode = models.CharField(choices=CHOICES_SSL_TLS_MODE, max_length=255, default='Off', null=True, blank=True)
    CHOICES_REQUIRE_TRUSTED_CERTIFICATE = [
        ("No", "No"),
        ("Yes", "Yes"),
    ]
    require_trusted_certificate = models.CharField(choices=CHOICES_REQUIRE_TRUSTED_CERTIFICATE, max_length=255, default='No', null=True, blank=True)
    local_private_key_file = models.CharField(max_length=255, null=True, blank=True)
    local_server_certificate_file = models.CharField(max_length=255, null=True, blank=True)
    local_ca_certs_file = models.CharField(max_length=255, null=True, blank=True)
    ldap_group_field = models.CharField(max_length=255, null=True, blank=True)
    ldap_groups = models.ManyToManyField("frappe_app.LdapGroupMapping", related_name="LDAPSettingsLdapGroups", )
    ldap_group_member_attribute = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_LDAP_DIRECTORY_SERVER = [
        ("Active Directory", "Active Directory"),
        ("OpenLDAP", "OpenLDAP"),
        ("Custom", "Custom"),
    ]
    ldap_directory_server = models.CharField(choices=CHOICES_LDAP_DIRECTORY_SERVER, max_length=255, null=True, blank=True)
    ldap_group_objectclass = models.CharField(max_length=255, null=True, blank=True)
    ldap_custom_group_search = models.CharField(max_length=255, null=True, blank=True)
    ldap_search_path_user = models.CharField(max_length=255, null=True, blank=True)
    ldap_search_path_group = models.CharField(max_length=255, null=True, blank=True)
    default_user_type = models.ForeignKey("frappe_app.UserType", related_name="LDAPSettingsDefaultUserType", on_delete=models.CASCADE, null=True, blank=True)
    do_not_create_new_user = models.BooleanField(default=False, null=True, blank=True)
