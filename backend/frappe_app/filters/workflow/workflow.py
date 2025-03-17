import django_filters as filters
from frappe_app.models.workflow.workflow import Workflow

class WorkflowFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Workflow
        fields = ['id']

