import django_filters as filters
from frappe_app.models.workflow.workflow_document_state import WorkflowDocumentState

class WorkflowDocumentStateFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WorkflowDocumentState
        fields = ['id']

