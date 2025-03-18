import django_filters as filters
from frappe_app.models.frappe_core.user_social_login import UserSocialLogin

class UserSocialLoginFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserSocialLogin
        fields = ['id']

