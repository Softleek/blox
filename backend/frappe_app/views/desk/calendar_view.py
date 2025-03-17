from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.calendar_view import CalendarView
from frappe_app.filters.desk.calendar_view import CalendarViewFilter
from frappe_app.serializers.desk.calendar_view import CalendarViewSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CalendarViewViewSet(GenericViewSet):
    queryset = CalendarView.objects.all()
    filterset_class = CalendarViewFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CalendarViewSerializer

