import django_filters as filters
from frappe_app.models.integrations.s3_backup_settings import S3BackupSettings

class S3BackupSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = S3BackupSettings
        fields = ['id']

