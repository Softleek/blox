from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.custom_html_block import CustomHTMLBlock

class CustomHTMLBlockSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = CustomHTMLBlock
        fields = '__all__'
