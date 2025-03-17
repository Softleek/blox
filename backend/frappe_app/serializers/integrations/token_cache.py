from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.token_cache import TokenCache

class TokenCacheSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = TokenCache
        fields = '__all__'
