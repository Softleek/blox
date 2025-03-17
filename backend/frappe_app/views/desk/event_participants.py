from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.event_participants import EventParticipants
from frappe_app.filters.desk.event_participants import EventParticipantsFilter
from frappe_app.serializers.desk.event_participants import EventParticipantsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EventParticipantsViewSet(GenericViewSet):
    queryset = EventParticipants.objects.all()
    filterset_class = EventParticipantsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EventParticipantsSerializer

