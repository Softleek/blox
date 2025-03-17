import django_filters as filters
from frappe_app.models.automation.assignment_rule_user import AssignmentRuleUser

class AssignmentRuleUserFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AssignmentRuleUser
        fields = ['id']

