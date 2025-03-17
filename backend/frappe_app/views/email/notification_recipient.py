from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.notification_recipient import NotificationRecipient
from frappe_app.filters.email.notification_recipient import NotificationRecipientFilter
from frappe_app.serializers.email.notification_recipient import NotificationRecipientSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NotificationRecipientViewSet(GenericViewSet):
    queryset = NotificationRecipient.objects.all()
    filterset_class = NotificationRecipientFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NotificationRecipientSerializer

