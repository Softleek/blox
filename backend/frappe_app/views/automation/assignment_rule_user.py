from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.automation.assignment_rule_user import AssignmentRuleUser
from frappe_app.filters.automation.assignment_rule_user import AssignmentRuleUserFilter
from frappe_app.serializers.automation.assignment_rule_user import AssignmentRuleUserSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AssignmentRuleUserViewSet(GenericViewSet):
    queryset = AssignmentRuleUser.objects.all()
    filterset_class = AssignmentRuleUserFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AssignmentRuleUserSerializer

