from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.communication_link import CommunicationLink
from frappe_app.filters.core.communication_link import CommunicationLinkFilter
from frappe_app.serializers.core.communication_link import CommunicationLinkSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CommunicationLinkViewSet(GenericViewSet):
    queryset = CommunicationLink.objects.all()
    filterset_class = CommunicationLinkFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CommunicationLinkSerializer

