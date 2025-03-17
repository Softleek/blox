import django_filters as filters
from frappe_app.models.core.role_profile import RoleProfile

class RoleProfileFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = RoleProfile
        fields = ['id']

