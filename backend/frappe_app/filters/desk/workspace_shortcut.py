import django_filters as filters
from frappe_app.models.desk.workspace_shortcut import WorkspaceShortcut

class WorkspaceShortcutFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkspaceShortcut
        fields = ['id']

