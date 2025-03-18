from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.document_naming_settings import DocumentNamingSettings

class DocumentNamingSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocumentNamingSettings
        fields = '__all__'
