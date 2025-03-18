from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.communication import Communication
from frappe_app.filters.frappe_core.communication import CommunicationFilter
from frappe_app.serializers.frappe_core.communication import CommunicationSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CommunicationViewSet(GenericViewSet):
    queryset = Communication.objects.all()
    filterset_class = CommunicationFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CommunicationSerializer

