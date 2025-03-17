from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.workspace_custom_block import WorkspaceCustomBlock

class WorkspaceCustomBlockSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkspaceCustomBlock
        fields = '__all__'
