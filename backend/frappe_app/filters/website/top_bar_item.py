import django_filters as filters
from frappe_app.models.website.top_bar_item import TopBarItem

class TopBarItemFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = TopBarItem
        fields = ['id']

