from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.printing.network_printer_settings import NetworkPrinterSettings

class NetworkPrinterSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NetworkPrinterSettings
        fields = '__all__'
