import django_filters as filters
from frappe_app.models.desk.system_health_report_queue import SystemHealthReportQueue

class SystemHealthReportQueueFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SystemHealthReportQueue
        fields = ['id']

