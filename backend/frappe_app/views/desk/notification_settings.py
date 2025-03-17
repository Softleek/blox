from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.notification_settings import NotificationSettings
from frappe_app.filters.desk.notification_settings import NotificationSettingsFilter
from frappe_app.serializers.desk.notification_settings import NotificationSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NotificationSettingsViewSet(GenericViewSet):
    queryset = NotificationSettings.objects.all()
    filterset_class = NotificationSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NotificationSettingsSerializer

