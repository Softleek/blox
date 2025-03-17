from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.scheduled_job_type import ScheduledJobType
from frappe_app.filters.core.scheduled_job_type import ScheduledJobTypeFilter
from frappe_app.serializers.core.scheduled_job_type import ScheduledJobTypeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ScheduledJobTypeViewSet(GenericViewSet):
    queryset = ScheduledJobType.objects.all()
    filterset_class = ScheduledJobTypeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ScheduledJobTypeSerializer

