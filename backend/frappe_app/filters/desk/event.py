import django_filters as filters
from frappe_app.models.desk.event import Event

class EventFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Event
        fields = ['id']

