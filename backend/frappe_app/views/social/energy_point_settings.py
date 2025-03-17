from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.social.energy_point_settings import EnergyPointSettings
from frappe_app.filters.social.energy_point_settings import EnergyPointSettingsFilter
from frappe_app.serializers.social.energy_point_settings import EnergyPointSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EnergyPointSettingsViewSet(GenericViewSet):
    queryset = EnergyPointSettings.objects.all()
    filterset_class = EnergyPointSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EnergyPointSettingsSerializer

