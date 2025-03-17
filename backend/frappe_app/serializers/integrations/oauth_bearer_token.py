from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.oauth_bearer_token import OAuthBearerToken

class OAuthBearerTokenSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = OAuthBearerToken
        fields = '__all__'
