import django_filters as filters
from frappe_app.models.integrations.token_cache import TokenCache

class TokenCacheFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = TokenCache
        fields = ['id']

