from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.notification import Notification
from frappe_app.filters.email.notification import NotificationFilter
from frappe_app.serializers.email.notification import NotificationSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NotificationViewSet(GenericViewSet):
    queryset = Notification.objects.all()
    filterset_class = NotificationFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NotificationSerializer

