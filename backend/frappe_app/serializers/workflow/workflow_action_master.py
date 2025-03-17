from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.workflow.workflow_action_master import WorkflowActionMaster

class WorkflowActionMasterSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkflowActionMaster
        fields = '__all__'
