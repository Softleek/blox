from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.user_group_member import UserGroupMember

class UserGroupMemberSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserGroupMember
        fields = '__all__'
