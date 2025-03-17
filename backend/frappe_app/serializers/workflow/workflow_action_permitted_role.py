from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.workflow.workflow_action_permitted_role import WorkflowActionPermittedRole

class WorkflowActionPermittedRoleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkflowActionPermittedRole
        fields = '__all__'
