import django_filters as filters
from frappe_app.models.desk.list_filter import ListFilter

class ListFilterFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ListFilter
        fields = ['id']

