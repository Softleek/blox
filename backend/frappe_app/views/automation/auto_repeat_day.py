from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.automation.auto_repeat_day import AutoRepeatDay
from frappe_app.filters.automation.auto_repeat_day import AutoRepeatDayFilter
from frappe_app.serializers.automation.auto_repeat_day import AutoRepeatDaySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AutoRepeatDayViewSet(GenericViewSet):
    queryset = AutoRepeatDay.objects.all()
    filterset_class = AutoRepeatDayFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AutoRepeatDaySerializer

