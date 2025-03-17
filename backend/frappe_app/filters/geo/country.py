import django_filters as filters
from frappe_app.models.geo.country import Country

class CountryFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Country
        fields = ['id']

