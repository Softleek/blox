import django_filters as filters
from frappe_app.models.social.energy_point_settings import EnergyPointSettings

class EnergyPointSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EnergyPointSettings
        fields = ['id']

