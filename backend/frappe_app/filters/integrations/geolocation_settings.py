import django_filters as filters
from frappe_app.models.integrations.geolocation_settings import GeolocationSettings

class GeolocationSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = GeolocationSettings
        fields = ['id']

