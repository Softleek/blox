from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.dashboard_chart_field import DashboardChartField
from frappe_app.filters.desk.dashboard_chart_field import DashboardChartFieldFilter
from frappe_app.serializers.desk.dashboard_chart_field import DashboardChartFieldSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DashboardChartFieldViewSet(GenericViewSet):
    queryset = DashboardChartField.objects.all()
    filterset_class = DashboardChartFieldFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DashboardChartFieldSerializer

