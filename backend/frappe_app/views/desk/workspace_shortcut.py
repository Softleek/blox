from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.workspace_shortcut import WorkspaceShortcut
from frappe_app.filters.desk.workspace_shortcut import WorkspaceShortcutFilter
from frappe_app.serializers.desk.workspace_shortcut import WorkspaceShortcutSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkspaceShortcutViewSet(GenericViewSet):
    queryset = WorkspaceShortcut.objects.all()
    filterset_class = WorkspaceShortcutFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkspaceShortcutSerializer

