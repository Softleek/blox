from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.amended_document_naming_settings import AmendedDocumentNamingSettings

class AmendedDocumentNamingSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AmendedDocumentNamingSettings
        fields = '__all__'
