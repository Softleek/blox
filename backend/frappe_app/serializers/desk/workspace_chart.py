from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.workspace_chart import WorkspaceChart

class WorkspaceChartSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkspaceChart
        fields = '__all__'
