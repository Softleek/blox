import django_filters as filters
from frappe_app.models.integrations.google_settings import GoogleSettings

class GoogleSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = GoogleSettings
        fields = ['id']

