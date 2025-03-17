from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.workspace_settings import WorkspaceSettings
from frappe_app.filters.desk.workspace_settings import WorkspaceSettingsFilter
from frappe_app.serializers.desk.workspace_settings import WorkspaceSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkspaceSettingsViewSet(GenericViewSet):
    queryset = WorkspaceSettings.objects.all()
    filterset_class = WorkspaceSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkspaceSettingsSerializer

