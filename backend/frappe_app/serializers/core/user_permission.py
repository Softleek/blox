from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.user_permission import UserPermission

class UserPermissionSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserPermission
        fields = '__all__'
