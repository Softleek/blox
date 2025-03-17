from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.user_select_document_type import UserSelectDocumentType

class UserSelectDocumentTypeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserSelectDocumentType
        fields = '__all__'
