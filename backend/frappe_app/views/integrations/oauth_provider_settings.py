from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.integrations.oauth_provider_settings import OAuthProviderSettings
from frappe_app.filters.integrations.oauth_provider_settings import OAuthProviderSettingsFilter
from frappe_app.serializers.integrations.oauth_provider_settings import OAuthProviderSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OAuthProviderSettingsViewSet(SingleInstanceViewSet):
    queryset = OAuthProviderSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = OAuthProviderSettingsSerializer

    filterset_class = OAuthProviderSettingsFilter
