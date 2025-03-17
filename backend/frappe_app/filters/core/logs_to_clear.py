import django_filters as filters
from frappe_app.models.core.logs_to_clear import LogsToClear

class LogsToClearFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = LogsToClear
        fields = ['id']

