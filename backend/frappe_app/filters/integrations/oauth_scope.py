import django_filters as filters
from frappe_app.models.integrations.oauth_scope import OAuthScope

class OAuthScopeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = OAuthScope
        fields = ['id']

