import django_filters as filters
from frappe_app.models.integrations.dropbox_settings import DropboxSettings

class DropboxSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DropboxSettings
        fields = ['id']

