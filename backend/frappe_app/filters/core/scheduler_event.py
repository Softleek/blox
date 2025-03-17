import django_filters as filters
from frappe_app.models.core.scheduler_event import SchedulerEvent

class SchedulerEventFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SchedulerEvent
        fields = ['id']

