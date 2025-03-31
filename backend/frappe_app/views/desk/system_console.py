from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.desk.system_console import SystemConsole
from frappe_app.filters.desk.system_console import SystemConsoleFilter
from frappe_app.serializers.desk.system_console import SystemConsoleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SystemConsoleViewSet(SingleInstanceViewSet):
    queryset = SystemConsole.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = SystemConsoleSerializer

    filterset_class = SystemConsoleFilter
