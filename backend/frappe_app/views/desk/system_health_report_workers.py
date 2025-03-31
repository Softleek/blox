from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.desk.system_health_report_workers import SystemHealthReportWorkers
from frappe_app.filters.desk.system_health_report_workers import SystemHealthReportWorkersFilter
from frappe_app.serializers.desk.system_health_report_workers import SystemHealthReportWorkersSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SystemHealthReportWorkersViewSet(GenericViewSet):
    queryset = SystemHealthReportWorkers.objects.all()
    filterset_class = SystemHealthReportWorkersFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SystemHealthReportWorkersSerializer

    filterset_class = SystemHealthReportWorkersFilter
