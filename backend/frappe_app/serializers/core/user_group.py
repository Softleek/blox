from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.user_group import UserGroup

class UserGroupSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserGroup
        fields = '__all__'
