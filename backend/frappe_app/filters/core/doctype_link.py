import django_filters as filters
from frappe_app.models.core.doctype_link import DocTypeLink

class DocTypeLinkFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocTypeLink
        fields = ['id']

