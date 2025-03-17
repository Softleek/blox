from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.ldap_group_mapping import LDAPGroupMapping
from frappe_app.filters.integrations.ldap_group_mapping import LDAPGroupMappingFilter
from frappe_app.serializers.integrations.ldap_group_mapping import LDAPGroupMappingSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class LDAPGroupMappingViewSet(GenericViewSet):
    queryset = LDAPGroupMapping.objects.all()
    filterset_class = LDAPGroupMappingFilter
    permission_classes = [HasGroupPermission]
    serializer_class = LDAPGroupMappingSerializer

