from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.dashboard_chart_source import DashboardChartSource
from frappe_app.filters.desk.dashboard_chart_source import DashboardChartSourceFilter
from frappe_app.serializers.desk.dashboard_chart_source import DashboardChartSourceSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DashboardChartSourceViewSet(GenericViewSet):
    queryset = DashboardChartSource.objects.all()
    filterset_class = DashboardChartSourceFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DashboardChartSourceSerializer

