from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.dashboard_chart_link import DashboardChartLink
from frappe_app.filters.desk.dashboard_chart_link import DashboardChartLinkFilter
from frappe_app.serializers.desk.dashboard_chart_link import DashboardChartLinkSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DashboardChartLinkViewSet(GenericViewSet):
    queryset = DashboardChartLink.objects.all()
    filterset_class = DashboardChartLinkFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DashboardChartLinkSerializer

