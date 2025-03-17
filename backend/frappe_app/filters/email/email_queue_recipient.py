import django_filters as filters
from frappe_app.models.email.email_queue_recipient import EmailQueueRecipient

class EmailQueueRecipientFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailQueueRecipient
        fields = ['id']

