import django_filters as filters
from frappe_app.models.integrations.oauth_client import OAuthClient

class OAuthClientFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = OAuthClient
        fields = ['id']

