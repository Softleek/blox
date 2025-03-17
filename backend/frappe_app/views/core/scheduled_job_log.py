from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.scheduled_job_log import ScheduledJobLog
from frappe_app.filters.core.scheduled_job_log import ScheduledJobLogFilter
from frappe_app.serializers.core.scheduled_job_log import ScheduledJobLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ScheduledJobLogViewSet(GenericViewSet):
    queryset = ScheduledJobLog.objects.all()
    filterset_class = ScheduledJobLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ScheduledJobLogSerializer

