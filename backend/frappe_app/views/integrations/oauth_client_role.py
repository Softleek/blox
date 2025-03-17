from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.oauth_client_role import OAuthClientRole
from frappe_app.filters.integrations.oauth_client_role import OAuthClientRoleFilter
from frappe_app.serializers.integrations.oauth_client_role import OAuthClientRoleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OAuthClientRoleViewSet(GenericViewSet):
    queryset = OAuthClientRole.objects.all()
    filterset_class = OAuthClientRoleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = OAuthClientRoleSerializer

