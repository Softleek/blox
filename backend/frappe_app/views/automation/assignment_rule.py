from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.automation.assignment_rule import AssignmentRule
from frappe_app.filters.automation.assignment_rule import AssignmentRuleFilter
from frappe_app.serializers.automation.assignment_rule import AssignmentRuleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AssignmentRuleViewSet(GenericViewSet):
    queryset = AssignmentRule.objects.all()
    filterset_class = AssignmentRuleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AssignmentRuleSerializer

