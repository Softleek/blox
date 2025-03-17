from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.workspace_settings import WorkspaceSettings

class WorkspaceSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkspaceSettings
        fields = '__all__'
