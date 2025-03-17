from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.workflow.workflow import Workflow
from frappe_app.filters.workflow.workflow import WorkflowFilter
from frappe_app.serializers.workflow.workflow import WorkflowSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WorkflowViewSet(GenericViewSet):
    queryset = Workflow.objects.all()
    filterset_class = WorkflowFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WorkflowSerializer

