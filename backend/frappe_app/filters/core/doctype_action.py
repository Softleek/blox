import django_filters as filters
from frappe_app.models.core.doctype_action import DocTypeAction

class DocTypeActionFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocTypeAction
        fields = ['id']

