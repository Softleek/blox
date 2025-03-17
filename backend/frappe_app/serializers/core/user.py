from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.user import User

class UserSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
