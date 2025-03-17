import django_filters as filters
from frappe_app.models.social.energy_point_log import EnergyPointLog

class EnergyPointLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EnergyPointLog
        fields = ['id']

