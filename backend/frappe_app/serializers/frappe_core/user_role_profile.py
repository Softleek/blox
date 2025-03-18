from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.user_role_profile import UserRoleProfile

class UserRoleProfileSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserRoleProfile
        fields = '__all__'
