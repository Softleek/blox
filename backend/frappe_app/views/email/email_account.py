from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_account import EmailAccount
from frappe_app.filters.email.email_account import EmailAccountFilter
from frappe_app.serializers.email.email_account import EmailAccountSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailAccountViewSet(GenericViewSet):
    queryset = EmailAccount.objects.all()
    filterset_class = EmailAccountFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailAccountSerializer

