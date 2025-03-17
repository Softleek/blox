import django_filters as filters
from frappe_app.models.desk.event_participants import EventParticipants

class EventParticipantsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EventParticipants
        fields = ['id']

