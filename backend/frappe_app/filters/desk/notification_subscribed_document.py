import django_filters as filters
from frappe_app.models.desk.notification_subscribed_document import NotificationSubscribedDocument

class NotificationSubscribedDocumentFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NotificationSubscribedDocument
        fields = ['id']

