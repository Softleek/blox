from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.oauth_bearer_token import OAuthBearerToken
from frappe_app.filters.integrations.oauth_bearer_token import OAuthBearerTokenFilter
from frappe_app.serializers.integrations.oauth_bearer_token import OAuthBearerTokenSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OAuthBearerTokenViewSet(GenericViewSet):
    queryset = OAuthBearerToken.objects.all()
    filterset_class = OAuthBearerTokenFilter
    permission_classes = [HasGroupPermission]
    serializer_class = OAuthBearerTokenSerializer

