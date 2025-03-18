import django_filters as filters
from frappe_app.models.frappe_core.role import Role

class RoleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Role
        fields = ['id']

