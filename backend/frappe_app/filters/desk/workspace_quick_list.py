import django_filters as filters
from frappe_app.models.desk.workspace_quick_list import WorkspaceQuickList

class WorkspaceQuickListFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkspaceQuickList
        fields = ['id']

