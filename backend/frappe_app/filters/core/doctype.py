import django_filters as filters
from frappe_app.models.core.doctype import DocType

class DocTypeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocType
        fields = ['id']

