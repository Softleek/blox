from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.console_log import ConsoleLog
from frappe_app.filters.desk.console_log import ConsoleLogFilter
from frappe_app.serializers.desk.console_log import ConsoleLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ConsoleLogViewSet(GenericViewSet):
    queryset = ConsoleLog.objects.all()
    filterset_class = ConsoleLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ConsoleLogSerializer

