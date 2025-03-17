import django_filters as filters
from frappe_app.models.automation.assignment_rule_day import AssignmentRuleDay

class AssignmentRuleDayFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AssignmentRuleDay
        fields = ['id']

