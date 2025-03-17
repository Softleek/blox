import django_filters as filters
from frappe_app.models.desk.number_card_link import NumberCardLink

class NumberCardLinkFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NumberCardLink
        fields = ['id']

