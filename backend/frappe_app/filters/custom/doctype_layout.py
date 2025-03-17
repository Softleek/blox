import django_filters as filters
from frappe_app.models.custom.doctype_layout import DocTypeLayout

class DocTypeLayoutFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocTypeLayout
        fields = ['id']

