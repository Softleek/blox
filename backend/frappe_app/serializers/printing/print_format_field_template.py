from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.printing.print_format_field_template import PrintFormatFieldTemplate

class PrintFormatFieldTemplateSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PrintFormatFieldTemplate
        fields = '__all__'
