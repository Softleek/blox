from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.s3_backup_settings import S3BackupSettings
from frappe_app.filters.integrations.s3_backup_settings import S3BackupSettingsFilter
from frappe_app.serializers.integrations.s3_backup_settings import S3BackupSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class S3BackupSettingsViewSet(GenericViewSet):
    queryset = S3BackupSettings.objects.all()
    filterset_class = S3BackupSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = S3BackupSettingsSerializer

