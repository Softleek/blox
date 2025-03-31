from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.desk.workspace_link import WorkspaceLink
from frappe_app.filters.desk.workspace_link import WorkspaceLinkFilter
from frappe_app.serializers.desk.workspace_link import WorkspaceLinkSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkspaceLinkViewSet(GenericViewSet):
    queryset = WorkspaceLink.objects.all()
    filterset_class = WorkspaceLinkFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkspaceLinkSerializer

    filterset_class = WorkspaceLinkFilter
