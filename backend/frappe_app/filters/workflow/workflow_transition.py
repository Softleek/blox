import django_filters as filters
from frappe_app.models.workflow.workflow_transition import WorkflowTransition

class WorkflowTransitionFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkflowTransition
        fields = ['id']

