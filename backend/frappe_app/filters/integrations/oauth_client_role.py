import django_filters as filters
from frappe_app.models.integrations.oauth_client_role import OAuthClientRole

class OAuthClientRoleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = OAuthClientRole
        fields = ['id']

