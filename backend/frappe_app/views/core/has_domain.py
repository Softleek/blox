from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.has_domain import HasDomain
from frappe_app.filters.core.has_domain import HasDomainFilter
from frappe_app.serializers.core.has_domain import HasDomainSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class HasDomainViewSet(GenericViewSet):
    queryset = HasDomain.objects.all()
    filterset_class = HasDomainFilter
    permission_classes = [HasGroupPermission]
    serializer_class = HasDomainSerializer

