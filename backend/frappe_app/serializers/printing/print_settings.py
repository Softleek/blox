from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.printing.print_settings import PrintSettings

class PrintSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PrintSettings
        fields = '__all__'
