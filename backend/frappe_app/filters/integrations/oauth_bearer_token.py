import django_filters as filters
from frappe_app.models.integrations.oauth_bearer_token import OAuthBearerToken

class OAuthBearerTokenFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = OAuthBearerToken
        fields = ['id']

