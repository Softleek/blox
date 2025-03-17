import django_filters as filters
from frappe_app.models.email.email_account import EmailAccount

class EmailAccountFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailAccount
        fields = ['id']

