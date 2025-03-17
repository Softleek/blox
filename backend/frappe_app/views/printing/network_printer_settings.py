from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.printing.network_printer_settings import NetworkPrinterSettings
from frappe_app.filters.printing.network_printer_settings import NetworkPrinterSettingsFilter
from frappe_app.serializers.printing.network_printer_settings import NetworkPrinterSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NetworkPrinterSettingsViewSet(GenericViewSet):
    queryset = NetworkPrinterSettings.objects.all()
    filterset_class = NetworkPrinterSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NetworkPrinterSettingsSerializer

