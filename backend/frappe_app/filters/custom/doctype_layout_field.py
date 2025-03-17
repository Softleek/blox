import django_filters as filters
from frappe_app.models.custom.doctype_layout_field import DocTypeLayoutField

class DocTypeLayoutFieldFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocTypeLayoutField
        fields = ['id']

