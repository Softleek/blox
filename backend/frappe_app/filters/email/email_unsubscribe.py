import django_filters as filters
from frappe_app.models.email.email_unsubscribe import EmailUnsubscribe

class EmailUnsubscribeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailUnsubscribe
        fields = ['id']

