from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.workflow.workflow_document_state import WorkflowDocumentState

class WorkflowDocumentStateSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkflowDocumentState
        fields = '__all__'
