from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.scheduler_event import SchedulerEvent
from frappe_app.filters.frappe_core.scheduler_event import SchedulerEventFilter
from frappe_app.serializers.frappe_core.scheduler_event import SchedulerEventSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SchedulerEventViewSet(GenericViewSet):
    queryset = SchedulerEvent.objects.all()
    filterset_class = SchedulerEventFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SchedulerEventSerializer

