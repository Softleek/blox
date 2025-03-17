import django_filters as filters
from frappe_app.models.email.email_flag_queue import EmailFlagQueue

class EmailFlagQueueFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailFlagQueue
        fields = ['id']

