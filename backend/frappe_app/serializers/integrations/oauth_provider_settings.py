from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.oauth_provider_settings import OAuthProviderSettings

class OAuthProviderSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = OAuthProviderSettings
        fields = '__all__'
