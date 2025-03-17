from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.system_console import SystemConsole
from frappe_app.filters.desk.system_console import SystemConsoleFilter
from frappe_app.serializers.desk.system_console import SystemConsoleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SystemConsoleViewSet(GenericViewSet):
    queryset = SystemConsole.objects.all()
    filterset_class = SystemConsoleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SystemConsoleSerializer

