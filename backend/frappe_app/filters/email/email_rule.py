import django_filters as filters
from frappe_app.models.email.email_rule import EmailRule

class EmailRuleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailRule
        fields = ['id']

