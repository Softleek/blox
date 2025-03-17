import django_filters as filters
from frappe_app.models.integrations.social_login_key import SocialLoginKey

class SocialLoginKeyFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SocialLoginKey
        fields = ['id']

