from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.document_follow import DocumentFollow

class DocumentFollowSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocumentFollow
        fields = '__all__'
