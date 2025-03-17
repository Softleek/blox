from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.role_profile import RoleProfile

class RoleProfileSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = RoleProfile
        fields = '__all__'
