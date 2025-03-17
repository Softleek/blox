import django_filters as filters
from frappe_app.models.core.has_role import HasRole

class HasRoleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = HasRole
        fields = ['id']

