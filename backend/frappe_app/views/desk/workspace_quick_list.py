from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.workspace_quick_list import WorkspaceQuickList
from frappe_app.filters.desk.workspace_quick_list import WorkspaceQuickListFilter
from frappe_app.serializers.desk.workspace_quick_list import WorkspaceQuickListSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkspaceQuickListViewSet(GenericViewSet):
    queryset = WorkspaceQuickList.objects.all()
    filterset_class = WorkspaceQuickListFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkspaceQuickListSerializer

