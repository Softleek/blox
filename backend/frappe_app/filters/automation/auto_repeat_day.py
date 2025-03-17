import django_filters as filters
from frappe_app.models.automation.auto_repeat_day import AutoRepeatDay

class AutoRepeatDayFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AutoRepeatDay
        fields = ['id']

