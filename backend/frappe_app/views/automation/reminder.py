from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.automation.reminder import Reminder
from frappe_app.filters.automation.reminder import ReminderFilter
from frappe_app.serializers.automation.reminder import ReminderSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ReminderViewSet(GenericViewSet):
    queryset = Reminder.objects.all()
    filterset_class = ReminderFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ReminderSerializer

