import django_filters as filters
from frappe_app.models.desk.notification_log import NotificationLog

class NotificationLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NotificationLog
        fields = ['id']

