import django_filters as filters
from frappe_app.models.integrations.ldap_group_mapping import LDAPGroupMapping

class LDAPGroupMappingFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = LDAPGroupMapping
        fields = ['id']

