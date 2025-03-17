from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.oauth_authorization_code import OAuthAuthorizationCode
from frappe_app.filters.integrations.oauth_authorization_code import OAuthAuthorizationCodeFilter
from frappe_app.serializers.integrations.oauth_authorization_code import OAuthAuthorizationCodeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OAuthAuthorizationCodeViewSet(GenericViewSet):
    queryset = OAuthAuthorizationCode.objects.all()
    filterset_class = OAuthAuthorizationCodeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = OAuthAuthorizationCodeSerializer

