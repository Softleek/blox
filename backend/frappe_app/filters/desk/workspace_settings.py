import django_filters as filters
from frappe_app.models.desk.workspace_settings import WorkspaceSettings

class WorkspaceSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkspaceSettings
        fields = ['id']

