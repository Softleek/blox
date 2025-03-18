import django_filters as filters
from frappe_app.models.frappe_core.user_group import UserGroup

class UserGroupFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserGroup
        fields = ['id']

