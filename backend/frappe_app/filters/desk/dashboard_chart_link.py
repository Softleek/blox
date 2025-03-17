import django_filters as filters
from frappe_app.models.desk.dashboard_chart_link import DashboardChartLink

class DashboardChartLinkFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DashboardChartLink
        fields = ['id']

