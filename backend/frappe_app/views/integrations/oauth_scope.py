from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.oauth_scope import OAuthScope
from frappe_app.filters.integrations.oauth_scope import OAuthScopeFilter
from frappe_app.serializers.integrations.oauth_scope import OAuthScopeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OAuthScopeViewSet(GenericViewSet):
    queryset = OAuthScope.objects.all()
    filterset_class = OAuthScopeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = OAuthScopeSerializer

