import django_filters as filters
from frappe_app.models.integrations.oauth_authorization_code import OAuthAuthorizationCode

class OAuthAuthorizationCodeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = OAuthAuthorizationCode
        fields = ['id']

