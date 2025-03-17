import django_filters as filters
from frappe_app.models.integrations.ldap_settings import LDAPSettings

class LDAPSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = LDAPSettings
        fields = ['id']

