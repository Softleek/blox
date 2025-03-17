from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.custom_role import CustomRole

class CustomRoleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = CustomRole
        fields = '__all__'
