from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.workspace_number_card import WorkspaceNumberCard

class WorkspaceNumberCardSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkspaceNumberCard
        fields = '__all__'
