import django_filters as filters
from frappe_app.models.workflow.workflow_action_permitted_role import WorkflowActionPermittedRole

class WorkflowActionPermittedRoleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkflowActionPermittedRole
        fields = ['id']

