import django_filters as filters
from frappe_app.models.desk.workspace_link import WorkspaceLink

class WorkspaceLinkFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkspaceLink
        fields = ['id']

