import django_filters as filters
from frappe_app.models.workflow.workflow_state import WorkflowState

class WorkflowStateFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkflowState
        fields = ['id']

