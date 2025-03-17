from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.notification_log import NotificationLog
from frappe_app.filters.desk.notification_log import NotificationLogFilter
from frappe_app.serializers.desk.notification_log import NotificationLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NotificationLogViewSet(GenericViewSet):
    queryset = NotificationLog.objects.all()
    filterset_class = NotificationLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NotificationLogSerializer

