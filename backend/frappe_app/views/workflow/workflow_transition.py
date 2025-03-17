from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.workflow.workflow_transition import WorkflowTransition
from frappe_app.filters.workflow.workflow_transition import WorkflowTransitionFilter
from frappe_app.serializers.workflow.workflow_transition import WorkflowTransitionSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkflowTransitionViewSet(GenericViewSet):
    queryset = WorkflowTransition.objects.all()
    filterset_class = WorkflowTransitionFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkflowTransitionSerializer

