import django_filters as filters
from frappe_app.models.frappe_core.user_group_member import UserGroupMember

class UserGroupMemberFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserGroupMember
        fields = ['id']

