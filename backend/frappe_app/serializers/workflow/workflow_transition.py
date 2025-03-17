from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.workflow.workflow_transition import WorkflowTransition

class WorkflowTransitionSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkflowTransition
        fields = '__all__'
