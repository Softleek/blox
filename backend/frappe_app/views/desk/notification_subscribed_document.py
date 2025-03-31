from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.desk.notification_subscribed_document import NotificationSubscribedDocument
from frappe_app.filters.desk.notification_subscribed_document import NotificationSubscribedDocumentFilter
from frappe_app.serializers.desk.notification_subscribed_document import NotificationSubscribedDocumentSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NotificationSubscribedDocumentViewSet(GenericViewSet):
    queryset = NotificationSubscribedDocument.objects.all()
    filterset_class = NotificationSubscribedDocumentFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NotificationSubscribedDocumentSerializer

    filterset_class = NotificationSubscribedDocumentFilter
