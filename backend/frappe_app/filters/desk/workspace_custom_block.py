import django_filters as filters
from frappe_app.models.desk.workspace_custom_block import WorkspaceCustomBlock

class WorkspaceCustomBlockFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkspaceCustomBlock
        fields = ['id']

