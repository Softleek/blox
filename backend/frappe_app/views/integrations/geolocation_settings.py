from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.geolocation_settings import GeolocationSettings
from frappe_app.filters.integrations.geolocation_settings import GeolocationSettingsFilter
from frappe_app.serializers.integrations.geolocation_settings import GeolocationSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GeolocationSettingsViewSet(GenericViewSet):
    queryset = GeolocationSettings.objects.all()
    filterset_class = GeolocationSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = GeolocationSettingsSerializer

