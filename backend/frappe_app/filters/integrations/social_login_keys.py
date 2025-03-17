import django_filters as filters
from frappe_app.models.integrations.social_login_keys import SocialLoginKeys

class SocialLoginKeysFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')


    class Meta:
        model = SocialLoginKeys
        fields = ['id']

