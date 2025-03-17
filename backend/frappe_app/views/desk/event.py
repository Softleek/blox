from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.event import Event
from frappe_app.filters.desk.event import EventFilter
from frappe_app.serializers.desk.event import EventSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EventViewSet(GenericViewSet):
    queryset = Event.objects.all()
    filterset_class = EventFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EventSerializer

