from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.user_social_login import UserSocialLogin

class UserSocialLoginSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserSocialLogin
        fields = '__all__'
