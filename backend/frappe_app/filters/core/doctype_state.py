import django_filters as filters
from frappe_app.models.core.doctype_state import DocTypeState

class DocTypeStateFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocTypeState
        fields = ['id']

