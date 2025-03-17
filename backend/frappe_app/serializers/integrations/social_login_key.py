from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.social_login_key import SocialLoginKey

class SocialLoginKeySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SocialLoginKey
        fields = '__all__'
