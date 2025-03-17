from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.push_notification_settings import PushNotificationSettings
from frappe_app.filters.integrations.push_notification_settings import PushNotificationSettingsFilter
from frappe_app.serializers.integrations.push_notification_settings import PushNotificationSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PushNotificationSettingsViewSet(GenericViewSet):
    queryset = PushNotificationSettings.objects.all()
    filterset_class = PushNotificationSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PushNotificationSettingsSerializer

