import django_filters as filters
from frappe_app.models.email.notification_recipient import NotificationRecipient

class NotificationRecipientFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NotificationRecipient
        fields = ['id']

