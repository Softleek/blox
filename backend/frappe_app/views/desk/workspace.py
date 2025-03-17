from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.workspace import Workspace
from frappe_app.filters.desk.workspace import WorkspaceFilter
from frappe_app.serializers.desk.workspace import WorkspaceSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkspaceViewSet(GenericViewSet):
    queryset = Workspace.objects.all()
    filterset_class = WorkspaceFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkspaceSerializer

