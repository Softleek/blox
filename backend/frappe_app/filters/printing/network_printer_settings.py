import django_filters as filters
from frappe_app.models.printing.network_printer_settings import NetworkPrinterSettings

class NetworkPrinterSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NetworkPrinterSettings
        fields = ['id']

