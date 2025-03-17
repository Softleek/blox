import django_filters as filters
from frappe_app.models.email.email_queue import EmailQueue

class EmailQueueFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailQueue
        fields = ['id']

