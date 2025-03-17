from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.workflow.workflow_action_master import WorkflowActionMaster
from frappe_app.filters.workflow.workflow_action_master import WorkflowActionMasterFilter
from frappe_app.serializers.workflow.workflow_action_master import WorkflowActionMasterSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkflowActionMasterViewSet(GenericViewSet):
    queryset = WorkflowActionMaster.objects.all()
    filterset_class = WorkflowActionMasterFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkflowActionMasterSerializer

