from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.workflow.workflow_action_permitted_role import WorkflowActionPermittedRole
from frappe_app.filters.workflow.workflow_action_permitted_role import WorkflowActionPermittedRoleFilter
from frappe_app.serializers.workflow.workflow_action_permitted_role import WorkflowActionPermittedRoleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkflowActionPermittedRoleViewSet(GenericViewSet):
    queryset = WorkflowActionPermittedRole.objects.all()
    filterset_class = WorkflowActionPermittedRoleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkflowActionPermittedRoleSerializer

