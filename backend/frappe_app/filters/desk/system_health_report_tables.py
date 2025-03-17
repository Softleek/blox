import django_filters as filters
from frappe_app.models.desk.system_health_report_tables import SystemHealthReportTables

class SystemHealthReportTablesFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SystemHealthReportTables
        fields = ['id']

