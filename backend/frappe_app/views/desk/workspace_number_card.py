from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.workspace_number_card import WorkspaceNumberCard
from frappe_app.filters.desk.workspace_number_card import WorkspaceNumberCardFilter
from frappe_app.serializers.desk.workspace_number_card import WorkspaceNumberCardSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkspaceNumberCardViewSet(GenericViewSet):
    queryset = WorkspaceNumberCard.objects.all()
    filterset_class = WorkspaceNumberCardFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkspaceNumberCardSerializer

