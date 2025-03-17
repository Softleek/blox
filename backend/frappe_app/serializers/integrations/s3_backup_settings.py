from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.s3_backup_settings import S3BackupSettings

class S3BackupSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = S3BackupSettings
        fields = '__all__'
