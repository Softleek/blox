from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_domain import EmailDomain
from frappe_app.filters.email.email_domain import EmailDomainFilter
from frappe_app.serializers.email.email_domain import EmailDomainSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailDomainViewSet(GenericViewSet):
    queryset = EmailDomain.objects.all()
    filterset_class = EmailDomainFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailDomainSerializer

