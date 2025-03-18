import django_filters as filters
from frappe_app.models.frappe_core.session_default_settings import SessionDefaultSettings

class SessionDefaultSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SessionDefaultSettings
        fields = ['id']

