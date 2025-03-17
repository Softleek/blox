import django_filters as filters
from frappe_app.models.automation.auto_repeat import AutoRepeat

class AutoRepeatFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AutoRepeat
        fields = ['id']

