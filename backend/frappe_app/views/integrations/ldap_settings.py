from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.ldap_settings import LDAPSettings
from frappe_app.filters.integrations.ldap_settings import LDAPSettingsFilter
from frappe_app.serializers.integrations.ldap_settings import LDAPSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class LDAPSettingsViewSet(GenericViewSet):
    queryset = LDAPSettings.objects.all()
    filterset_class = LDAPSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = LDAPSettingsSerializer

