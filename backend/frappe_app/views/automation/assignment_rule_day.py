from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.automation.assignment_rule_day import AssignmentRuleDay
from frappe_app.filters.automation.assignment_rule_day import AssignmentRuleDayFilter
from frappe_app.serializers.automation.assignment_rule_day import AssignmentRuleDaySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AssignmentRuleDayViewSet(GenericViewSet):
    queryset = AssignmentRuleDay.objects.all()
    filterset_class = AssignmentRuleDayFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AssignmentRuleDaySerializer

