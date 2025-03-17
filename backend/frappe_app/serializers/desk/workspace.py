from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.workspace import Workspace

class WorkspaceSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Workspace
        fields = '__all__'
