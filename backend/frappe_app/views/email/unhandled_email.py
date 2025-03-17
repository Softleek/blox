from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.unhandled_email import UnhandledEmail
from frappe_app.filters.email.unhandled_email import UnhandledEmailFilter
from frappe_app.serializers.email.unhandled_email import UnhandledEmailSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UnhandledEmailViewSet(GenericViewSet):
    queryset = UnhandledEmail.objects.all()
    filterset_class = UnhandledEmailFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UnhandledEmailSerializer

