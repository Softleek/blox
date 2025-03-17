from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.permission_log import PermissionLog

class PermissionLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PermissionLog
        fields = '__all__'
