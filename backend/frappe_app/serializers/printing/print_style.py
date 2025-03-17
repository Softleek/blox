from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.printing.print_style import PrintStyle

class PrintStyleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PrintStyle
        fields = '__all__'
