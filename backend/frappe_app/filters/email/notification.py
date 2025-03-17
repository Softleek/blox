import django_filters as filters
from frappe_app.models.email.notification import Notification

class NotificationFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Notification
        fields = ['id']

