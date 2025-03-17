from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.social_login_keys import SocialLoginKeys

class SocialLoginKeysSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SocialLoginKeys
        fields = '__all__'
