from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.custom.doctype_layout import DocTypeLayout

class DocTypeLayoutSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocTypeLayout
        fields = '__all__'
