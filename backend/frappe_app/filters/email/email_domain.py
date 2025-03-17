import django_filters as filters
from frappe_app.models.email.email_domain import EmailDomain

class EmailDomainFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailDomain
        fields = ['id']

