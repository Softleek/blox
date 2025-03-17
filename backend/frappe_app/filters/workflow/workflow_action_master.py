import django_filters as filters
from frappe_app.models.workflow.workflow_action_master import WorkflowActionMaster

class WorkflowActionMasterFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkflowActionMaster
        fields = ['id']

