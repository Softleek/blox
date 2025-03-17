import django_filters as filters
from frappe_app.models.core.dynamic_link import DynamicLink

class DynamicLinkFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DynamicLink
        fields = ['id']

