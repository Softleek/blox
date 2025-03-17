from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.workspace_custom_block import WorkspaceCustomBlock
from frappe_app.filters.desk.workspace_custom_block import WorkspaceCustomBlockFilter
from frappe_app.serializers.desk.workspace_custom_block import WorkspaceCustomBlockSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkspaceCustomBlockViewSet(GenericViewSet):
    queryset = WorkspaceCustomBlock.objects.all()
    filterset_class = WorkspaceCustomBlockFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkspaceCustomBlockSerializer

