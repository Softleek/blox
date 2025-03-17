from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.integration_request import IntegrationRequest
from frappe_app.filters.integrations.integration_request import IntegrationRequestFilter
from frappe_app.serializers.integrations.integration_request import IntegrationRequestSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class IntegrationRequestViewSet(GenericViewSet):
    queryset = IntegrationRequest.objects.all()
    filterset_class = IntegrationRequestFilter
    permission_classes = [HasGroupPermission]
    serializer_class = IntegrationRequestSerializer

