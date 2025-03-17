import django_filters as filters
from frappe_app.models.core.system_settings import SystemSettings

class SystemSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SystemSettings
        fields = ['id']

