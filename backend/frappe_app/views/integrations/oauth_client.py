from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.oauth_client import OAuthClient
from frappe_app.filters.integrations.oauth_client import OAuthClientFilter
from frappe_app.serializers.integrations.oauth_client import OAuthClientSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OAuthClientViewSet(GenericViewSet):
    queryset = OAuthClient.objects.all()
    filterset_class = OAuthClientFilter
    permission_classes = [HasGroupPermission]
    serializer_class = OAuthClientSerializer

