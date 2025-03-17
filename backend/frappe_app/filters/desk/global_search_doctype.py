import django_filters as filters
from frappe_app.models.desk.global_search_doctype import GlobalSearchDocType

class GlobalSearchDocTypeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = GlobalSearchDocType
        fields = ['id']

