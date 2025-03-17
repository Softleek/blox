from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.oauth_authorization_code import OAuthAuthorizationCode

class OAuthAuthorizationCodeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = OAuthAuthorizationCode
        fields = '__all__'
