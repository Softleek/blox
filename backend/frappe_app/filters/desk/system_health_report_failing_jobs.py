import django_filters as filters
from frappe_app.models.desk.system_health_report_failing_jobs import SystemHealthReportFailingJobs

class SystemHealthReportFailingJobsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SystemHealthReportFailingJobs
        fields = ['id']

