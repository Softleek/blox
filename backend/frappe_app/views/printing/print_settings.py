from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.printing.print_settings import PrintSettings
from frappe_app.filters.printing.print_settings import PrintSettingsFilter
from frappe_app.serializers.printing.print_settings import PrintSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PrintSettingsViewSet(GenericViewSet):
    queryset = PrintSettings.objects.all()
    filterset_class = PrintSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PrintSettingsSerializer

