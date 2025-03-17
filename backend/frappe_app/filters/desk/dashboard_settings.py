import django_filters as filters
from frappe_app.models.desk.dashboard_settings import DashboardSettings

class DashboardSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DashboardSettings
        fields = ['id']

