import django_filters as filters
from frappe_app.models.geo.currency import Currency

class CurrencyFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Currency
        fields = ['id']

