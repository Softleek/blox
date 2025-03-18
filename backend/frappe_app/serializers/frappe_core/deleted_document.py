from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.deleted_document import DeletedDocument

class DeletedDocumentSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DeletedDocument
        fields = '__all__'
