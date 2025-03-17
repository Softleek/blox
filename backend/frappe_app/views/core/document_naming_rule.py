from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.document_naming_rule import DocumentNamingRule
from frappe_app.filters.core.document_naming_rule import DocumentNamingRuleFilter
from frappe_app.serializers.core.document_naming_rule import DocumentNamingRuleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocumentNamingRuleViewSet(GenericViewSet):
    queryset = DocumentNamingRule.objects.all()
    filterset_class = DocumentNamingRuleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocumentNamingRuleSerializer

