from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.dashboard_chart import DashboardChart
from frappe_app.filters.desk.dashboard_chart import DashboardChartFilter
from frappe_app.serializers.desk.dashboard_chart import DashboardChartSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DashboardChartViewSet(GenericViewSet):
    queryset = DashboardChart.objects.all()
    filterset_class = DashboardChartFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DashboardChartSerializer

