from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.user_type import UserType

class UserTypeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserType
        fields = '__all__'
