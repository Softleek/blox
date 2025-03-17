import django_filters as filters
from frappe_app.models.desk.dashboard_chart_field import DashboardChartField

class DashboardChartFieldFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DashboardChartField
        fields = ['id']

