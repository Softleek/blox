from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.connected_app import ConnectedApp
from frappe_app.filters.integrations.connected_app import ConnectedAppFilter
from frappe_app.serializers.integrations.connected_app import ConnectedAppSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ConnectedAppViewSet(GenericViewSet):
    queryset = ConnectedApp.objects.all()
    filterset_class = ConnectedAppFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ConnectedAppSerializer

