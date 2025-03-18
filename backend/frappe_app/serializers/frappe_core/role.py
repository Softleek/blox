from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.role import Role

class RoleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'
