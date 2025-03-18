import django_filters as filters
from frappe_app.models.frappe_core.docperm import DocPerm

class DocPermFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocPerm
        fields = ['id']

