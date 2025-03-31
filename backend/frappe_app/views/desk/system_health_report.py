from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.desk.system_health_report import SystemHealthReport
from frappe_app.filters.desk.system_health_report import SystemHealthReportFilter
from frappe_app.serializers.desk.system_health_report import SystemHealthReportSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SystemHealthReportViewSet(SingleInstanceViewSet):
    queryset = SystemHealthReport.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = SystemHealthReportSerializer

    filterset_class = SystemHealthReportFilter
