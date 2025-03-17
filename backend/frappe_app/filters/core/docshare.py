import django_filters as filters
from frappe_app.models.core.docshare import DocShare

class DocShareFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocShare
        fields = ['id']

