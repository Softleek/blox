from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.workflow.workflow_state import WorkflowState

class WorkflowStateSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkflowState
        fields = '__all__'
