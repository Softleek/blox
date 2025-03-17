from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.system_health_report_queue import SystemHealthReportQueue
from frappe_app.filters.desk.system_health_report_queue import SystemHealthReportQueueFilter
from frappe_app.serializers.desk.system_health_report_queue import SystemHealthReportQueueSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SystemHealthReportQueueViewSet(GenericViewSet):
    queryset = SystemHealthReportQueue.objects.all()
    filterset_class = SystemHealthReportQueueFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SystemHealthReportQueueSerializer

