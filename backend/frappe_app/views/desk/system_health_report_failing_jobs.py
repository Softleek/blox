from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.system_health_report_failing_jobs import SystemHealthReportFailingJobs
from frappe_app.filters.desk.system_health_report_failing_jobs import SystemHealthReportFailingJobsFilter
from frappe_app.serializers.desk.system_health_report_failing_jobs import SystemHealthReportFailingJobsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SystemHealthReportFailingJobsViewSet(GenericViewSet):
    queryset = SystemHealthReportFailingJobs.objects.all()
    filterset_class = SystemHealthReportFailingJobsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SystemHealthReportFailingJobsSerializer

