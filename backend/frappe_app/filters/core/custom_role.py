import django_filters as filters
from frappe_app.models.core.custom_role import CustomRole

class CustomRoleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = CustomRole
        fields = ['id']

