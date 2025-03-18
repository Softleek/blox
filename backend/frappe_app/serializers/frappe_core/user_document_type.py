from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.user_document_type import UserDocumentType

class UserDocumentTypeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserDocumentType
        fields = '__all__'
