from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.oauth_scope import OAuthScope

class OAuthScopeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = OAuthScope
        fields = '__all__'
