import django_filters as filters
from frappe_app.models.integrations.push_notification_settings import PushNotificationSettings

class PushNotificationSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PushNotificationSettings
        fields = ['id']

