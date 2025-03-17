import django_filters as filters
from frappe_app.models.social.energy_point_rule import EnergyPointRule

class EnergyPointRuleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EnergyPointRule
        fields = ['id']

