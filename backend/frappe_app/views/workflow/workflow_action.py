from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.workflow.workflow_action import WorkflowAction
from frappe_app.filters.workflow.workflow_action import WorkflowActionFilter
from frappe_app.serializers.workflow.workflow_action import WorkflowActionSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkflowActionViewSet(GenericViewSet):
    queryset = WorkflowAction.objects.all()
    filterset_class = WorkflowActionFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkflowActionSerializer

