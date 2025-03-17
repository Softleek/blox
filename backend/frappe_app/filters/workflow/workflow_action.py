import django_filters as filters
from frappe_app.models.workflow.workflow_action import WorkflowAction

class WorkflowActionFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkflowAction
        fields = ['id']

