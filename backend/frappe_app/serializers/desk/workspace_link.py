from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.workspace_link import WorkspaceLink

class WorkspaceLinkSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkspaceLink
        fields = '__all__'
