from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.portal_settings import PortalSettings
from frappe_app.filters.website.portal_settings import PortalSettingsFilter
from frappe_app.serializers.website.portal_settings import PortalSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PortalSettingsViewSet(GenericViewSet):
    queryset = PortalSettings.objects.all()
    filterset_class = PortalSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PortalSettingsSerializer

