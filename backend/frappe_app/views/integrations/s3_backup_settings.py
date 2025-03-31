from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.integrations.s3_backup_settings import S3BackupSettings
from frappe_app.filters.integrations.s3_backup_settings import S3BackupSettingsFilter
from frappe_app.serializers.integrations.s3_backup_settings import S3BackupSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class S3BackupSettingsViewSet(SingleInstanceViewSet):
    queryset = S3BackupSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = S3BackupSettingsSerializer

    filterset_class = S3BackupSettingsFilter
