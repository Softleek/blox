import django_filters as filters
from frappe_app.models.frappe_core.recorder_suggested_index import RecorderSuggestedIndex

class RecorderSuggestedIndexFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = RecorderSuggestedIndex
        fields = ['id']

