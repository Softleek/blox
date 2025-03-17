from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.workflow.workflow_state import WorkflowState
from frappe_app.filters.workflow.workflow_state import WorkflowStateFilter
from frappe_app.serializers.workflow.workflow_state import WorkflowStateSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkflowStateViewSet(GenericViewSet):
    queryset = WorkflowState.objects.all()
    filterset_class = WorkflowStateFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkflowStateSerializer

