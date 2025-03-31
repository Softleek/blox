from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.integrations.ldap_settings import LDAPSettings
from frappe_app.filters.integrations.ldap_settings import LDAPSettingsFilter
from frappe_app.serializers.integrations.ldap_settings import LDAPSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class LDAPSettingsViewSet(SingleInstanceViewSet):
    queryset = LDAPSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = LDAPSettingsSerializer

    filterset_class = LDAPSettingsFilter
