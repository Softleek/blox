from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.domain import Domain
from frappe_app.filters.frappe_core.domain import DomainFilter
from frappe_app.serializers.frappe_core.domain import DomainSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DomainViewSet(GenericViewSet):
    queryset = Domain.objects.all()
    filterset_class = DomainFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DomainSerializer

