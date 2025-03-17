import django_filters as filters
from frappe_app.models.desk.notification_settings import NotificationSettings

class NotificationSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NotificationSettings
        fields = ['id']

