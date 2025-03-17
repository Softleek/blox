from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.data_import import DataImport

class DataImportSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DataImport
        fields = '__all__'
