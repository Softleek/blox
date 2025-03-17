import django_filters as filters
from frappe_app.models.core.document_naming_rule import DocumentNamingRule

class DocumentNamingRuleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocumentNamingRule
        fields = ['id']

