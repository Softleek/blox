import django_filters as filters
from frappe_app.models.desk.workspace_chart import WorkspaceChart

class WorkspaceChartFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkspaceChart
        fields = ['id']

