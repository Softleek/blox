import django_filters as filters
from frappe_app.models.core.recorder_suggested_index import RecorderSuggestedIndex

class RecorderSuggestedIndexFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = RecorderSuggestedIndex
        fields = ['id']

