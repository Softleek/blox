from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.system_health_report_tables import SystemHealthReportTables
from frappe_app.filters.desk.system_health_report_tables import SystemHealthReportTablesFilter
from frappe_app.serializers.desk.system_health_report_tables import SystemHealthReportTablesSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SystemHealthReportTablesViewSet(GenericViewSet):
    queryset = SystemHealthReportTables.objects.all()
    filterset_class = SystemHealthReportTablesFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SystemHealthReportTablesSerializer

