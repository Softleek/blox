from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.workflow.workflow_document_state import WorkflowDocumentState
from frappe_app.filters.workflow.workflow_document_state import WorkflowDocumentStateFilter
from frappe_app.serializers.workflow.workflow_document_state import WorkflowDocumentStateSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkflowDocumentStateViewSet(GenericViewSet):
    queryset = WorkflowDocumentState.objects.all()
    filterset_class = WorkflowDocumentStateFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkflowDocumentStateSerializer

