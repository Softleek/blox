import django_filters as filters
from frappe_app.models.desk.system_health_report import SystemHealthReport

class SystemHealthReportFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SystemHealthReport
        fields = ['id']

