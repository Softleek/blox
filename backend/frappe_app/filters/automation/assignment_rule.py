import django_filters as filters
from frappe_app.models.automation.assignment_rule import AssignmentRule

class AssignmentRuleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AssignmentRule
        fields = ['id']

