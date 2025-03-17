from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.oauth_client_role import OAuthClientRole

class OAuthClientRoleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = OAuthClientRole
        fields = '__all__'
