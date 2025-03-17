from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.oauth_provider_settings import OAuthProviderSettings
from frappe_app.filters.integrations.oauth_provider_settings import OAuthProviderSettingsFilter
from frappe_app.serializers.integrations.oauth_provider_settings import OAuthProviderSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OAuthProviderSettingsViewSet(GenericViewSet):
    queryset = OAuthProviderSettings.objects.all()
    filterset_class = OAuthProviderSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = OAuthProviderSettingsSerializer

