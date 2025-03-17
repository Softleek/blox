from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_flag_queue import EmailFlagQueue
from frappe_app.filters.email.email_flag_queue import EmailFlagQueueFilter
from frappe_app.serializers.email.email_flag_queue import EmailFlagQueueSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailFlagQueueViewSet(GenericViewSet):
    queryset = EmailFlagQueue.objects.all()
    filterset_class = EmailFlagQueueFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailFlagQueueSerializer

