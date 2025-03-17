from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.data_export import DataExport

class DataExportSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DataExport
        fields = '__all__'
