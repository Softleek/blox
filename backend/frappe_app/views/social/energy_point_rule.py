from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.social.energy_point_rule import EnergyPointRule
from frappe_app.filters.social.energy_point_rule import EnergyPointRuleFilter
from frappe_app.serializers.social.energy_point_rule import EnergyPointRuleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EnergyPointRuleViewSet(GenericViewSet):
    queryset = EnergyPointRule.objects.all()
    filterset_class = EnergyPointRuleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EnergyPointRuleSerializer

