import django_filters as filters
from frappe_app.models.desk.system_health_report_errors import SystemHealthReportErrors

class SystemHealthReportErrorsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SystemHealthReportErrors
        fields = ['id']

