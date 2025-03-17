import django_filters as filters
from frappe_app.models.desk.workspace_number_card import WorkspaceNumberCard

class WorkspaceNumberCardFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkspaceNumberCard
        fields = ['id']

