import django_filters as filters
from frappe_app.models.frappe_core.log_settings import LogSettings

class LogSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = LogSettings
        fields = ['id']

