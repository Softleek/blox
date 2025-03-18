import django_filters as filters
from frappe_app.models.frappe_core.user_role_profile import UserRoleProfile

class UserRoleProfileFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserRoleProfile
        fields = ['id']

