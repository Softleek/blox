import django_filters as filters
from frappe_app.models.frappe_core.recorder import Recorder

class RecorderFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Recorder
        fields = ['id']

