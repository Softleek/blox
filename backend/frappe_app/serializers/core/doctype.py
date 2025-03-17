from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.doctype import DocType

class DocTypeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocType
        fields = '__all__'
