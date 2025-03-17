from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.workflow.workflow import Workflow

class WorkflowSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Workflow
        fields = '__all__'
