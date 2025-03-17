from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.document_naming_rule_condition import DocumentNamingRuleCondition
from frappe_app.filters.core.document_naming_rule_condition import DocumentNamingRuleConditionFilter
from frappe_app.serializers.core.document_naming_rule_condition import DocumentNamingRuleConditionSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocumentNamingRuleConditionViewSet(GenericViewSet):
    queryset = DocumentNamingRuleCondition.objects.all()
    filterset_class = DocumentNamingRuleConditionFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocumentNamingRuleConditionSerializer

