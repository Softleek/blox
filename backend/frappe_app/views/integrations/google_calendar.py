from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.integrations.google_calendar import GoogleCalendar
from frappe_app.filters.integrations.google_calendar import GoogleCalendarFilter
from frappe_app.serializers.integrations.google_calendar import GoogleCalendarSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GoogleCalendarViewSet(GenericViewSet):
    queryset = GoogleCalendar.objects.all()
    filterset_class = GoogleCalendarFilter
    permission_classes = [HasGroupPermission]
    serializer_class = GoogleCalendarSerializer

    filterset_class = GoogleCalendarFilter
