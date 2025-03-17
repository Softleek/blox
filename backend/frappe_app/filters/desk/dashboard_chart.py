import django_filters as filters
from frappe_app.models.desk.dashboard_chart import DashboardChart

class DashboardChartFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DashboardChart
        fields = ['id']

