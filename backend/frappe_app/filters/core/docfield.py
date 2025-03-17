import django_filters as filters
from frappe_app.models.core.docfield import DocField

class DocFieldFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocField
        fields = ['id']

