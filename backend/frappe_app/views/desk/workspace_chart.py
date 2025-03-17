from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.workspace_chart import WorkspaceChart
from frappe_app.filters.desk.workspace_chart import WorkspaceChartFilter
from frappe_app.serializers.desk.workspace_chart import WorkspaceChartSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkspaceChartViewSet(GenericViewSet):
    queryset = WorkspaceChart.objects.all()
    filterset_class = WorkspaceChartFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkspaceChartSerializer

