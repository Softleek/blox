import django_filters as filters
from frappe_app.models.desk.dashboard_chart_source import DashboardChartSource

class DashboardChartSourceFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DashboardChartSource
        fields = ['id']

