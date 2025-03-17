import django_filters as filters
from frappe_app.models.integrations.oauth_provider_settings import OAuthProviderSettings

class OAuthProviderSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = OAuthProviderSettings
        fields = ['id']

