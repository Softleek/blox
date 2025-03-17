from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.token_cache import TokenCache
from frappe_app.filters.integrations.token_cache import TokenCacheFilter
from frappe_app.serializers.integrations.token_cache import TokenCacheSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class TokenCacheViewSet(GenericViewSet):
    queryset = TokenCache.objects.all()
    filterset_class = TokenCacheFilter
    permission_classes = [HasGroupPermission]
    serializer_class = TokenCacheSerializer

