from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.integrations.geolocation_settings import GeolocationSettings
from frappe_app.filters.integrations.geolocation_settings import GeolocationSettingsFilter
from frappe_app.serializers.integrations.geolocation_settings import GeolocationSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GeolocationSettingsViewSet(SingleInstanceViewSet):
    queryset = GeolocationSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = GeolocationSettingsSerializer

    filterset_class = GeolocationSettingsFilter
