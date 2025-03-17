from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_queue_recipient import EmailQueueRecipient
from frappe_app.filters.email.email_queue_recipient import EmailQueueRecipientFilter
from frappe_app.serializers.email.email_queue_recipient import EmailQueueRecipientSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailQueueRecipientViewSet(GenericViewSet):
    queryset = EmailQueueRecipient.objects.all()
    filterset_class = EmailQueueRecipientFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailQueueRecipientSerializer

