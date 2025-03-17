import django_filters as filters
from frappe_app.models.desk.number_card import NumberCard

class NumberCardFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NumberCard
        fields = ['id']

