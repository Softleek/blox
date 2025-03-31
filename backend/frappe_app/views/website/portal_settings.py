from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.website.portal_settings import PortalSettings
from frappe_app.filters.website.portal_settings import PortalSettingsFilter
from frappe_app.serializers.website.portal_settings import PortalSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PortalSettingsViewSet(SingleInstanceViewSet):
    queryset = PortalSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = PortalSettingsSerializer

    filterset_class = PortalSettingsFilter
