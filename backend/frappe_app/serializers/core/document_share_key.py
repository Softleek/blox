from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.document_share_key import DocumentShareKey

class DocumentShareKeySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocumentShareKey
        fields = '__all__'
