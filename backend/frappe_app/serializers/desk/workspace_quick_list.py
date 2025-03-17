from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.workspace_quick_list import WorkspaceQuickList

class WorkspaceQuickListSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkspaceQuickList
        fields = '__all__'
