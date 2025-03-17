from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.social.energy_point_log import EnergyPointLog
from frappe_app.filters.social.energy_point_log import EnergyPointLogFilter
from frappe_app.serializers.social.energy_point_log import EnergyPointLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EnergyPointLogViewSet(GenericViewSet):
    queryset = EnergyPointLog.objects.all()
    filterset_class = EnergyPointLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EnergyPointLogSerializer

