from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.system_health_report_errors import SystemHealthReportErrors
from frappe_app.filters.desk.system_health_report_errors import SystemHealthReportErrorsFilter
from frappe_app.serializers.desk.system_health_report_errors import SystemHealthReportErrorsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SystemHealthReportErrorsViewSet(GenericViewSet):
    queryset = SystemHealthReportErrors.objects.all()
    filterset_class = SystemHealthReportErrorsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SystemHealthReportErrorsSerializer

