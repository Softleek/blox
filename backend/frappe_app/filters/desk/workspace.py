import django_filters as filters
from frappe_app.models.desk.workspace import Workspace

class WorkspaceFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Workspace
        fields = ['id']

