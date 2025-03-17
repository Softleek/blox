from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.workspace_shortcut import WorkspaceShortcut

class WorkspaceShortcutSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkspaceShortcut
        fields = '__all__'
