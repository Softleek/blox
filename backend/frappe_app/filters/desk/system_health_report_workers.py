import django_filters as filters
from frappe_app.models.desk.system_health_report_workers import SystemHealthReportWorkers

class SystemHealthReportWorkersFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SystemHealthReportWorkers
        fields = ['id']

