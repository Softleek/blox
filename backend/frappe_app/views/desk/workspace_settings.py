from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.desk.workspace_settings import WorkspaceSettings
from frappe_app.filters.desk.workspace_settings import WorkspaceSettingsFilter
from frappe_app.serializers.desk.workspace_settings import WorkspaceSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkspaceSettingsViewSet(SingleInstanceViewSet):
    queryset = WorkspaceSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = WorkspaceSettingsSerializer

    filterset_class = WorkspaceSettingsFilter
