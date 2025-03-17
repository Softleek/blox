import django_filters as filters
from frappe_app.models.core.recorder_query import RecorderQuery

class RecorderQueryFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = RecorderQuery
        fields = ['id']

