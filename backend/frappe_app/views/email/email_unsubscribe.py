from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_unsubscribe import EmailUnsubscribe
from frappe_app.filters.email.email_unsubscribe import EmailUnsubscribeFilter
from frappe_app.serializers.email.email_unsubscribe import EmailUnsubscribeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailUnsubscribeViewSet(GenericViewSet):
    queryset = EmailUnsubscribe.objects.all()
    filterset_class = EmailUnsubscribeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailUnsubscribeSerializer

