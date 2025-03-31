from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.printing.print_settings import PrintSettings
from frappe_app.filters.printing.print_settings import PrintSettingsFilter
from frappe_app.serializers.printing.print_settings import PrintSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PrintSettingsViewSet(SingleInstanceViewSet):
    queryset = PrintSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = PrintSettingsSerializer

    filterset_class = PrintSettingsFilter
