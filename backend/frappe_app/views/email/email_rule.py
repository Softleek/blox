from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_rule import EmailRule
from frappe_app.filters.email.email_rule import EmailRuleFilter
from frappe_app.serializers.email.email_rule import EmailRuleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailRuleViewSet(GenericViewSet):
    queryset = EmailRule.objects.all()
    filterset_class = EmailRuleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailRuleSerializer

