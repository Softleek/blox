from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.permission_inspector import PermissionInspector

class PermissionInspectorSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PermissionInspector
        fields = '__all__'
