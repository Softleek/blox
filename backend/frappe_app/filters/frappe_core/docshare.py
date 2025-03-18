import django_filters as filters
from frappe_app.models.frappe_core.docshare import DocShare

class DocShareFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocShare
        fields = ['id']

