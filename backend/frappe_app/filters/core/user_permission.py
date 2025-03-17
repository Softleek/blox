import django_filters as filters
from frappe_app.models.core.user_permission import UserPermission

class UserPermissionFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserPermission
        fields = ['id']

