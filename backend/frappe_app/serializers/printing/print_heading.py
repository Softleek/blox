from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.printing.print_heading import PrintHeading

class PrintHeadingSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PrintHeading
        fields = '__all__'
