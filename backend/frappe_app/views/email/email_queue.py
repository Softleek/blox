from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_queue import EmailQueue
from frappe_app.filters.email.email_queue import EmailQueueFilter
from frappe_app.serializers.email.email_queue import EmailQueueSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailQueueViewSet(GenericViewSet):
    queryset = EmailQueue.objects.all()
    filterset_class = EmailQueueFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailQueueSerializer

