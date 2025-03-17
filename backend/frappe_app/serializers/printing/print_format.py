from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.printing.print_format import PrintFormat

class PrintFormatSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PrintFormat
        fields = '__all__'
