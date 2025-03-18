from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.data_import_log import DataImportLog

class DataImportLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DataImportLog
        fields = '__all__'
