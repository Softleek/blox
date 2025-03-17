import django_filters as filters
from frappe_app.models.core.document_naming_rule_condition import DocumentNamingRuleCondition

class DocumentNamingRuleConditionFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocumentNamingRuleCondition
        fields = ['id']

