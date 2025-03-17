import django_filters as filters
from frappe_app.models.desk.dashboard import Dashboard

class DashboardFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Dashboard
        fields = ['id']

