from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.user_type_module import UserTypeModule

class UserTypeModuleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserTypeModule
        fields = '__all__'
