import django_filters as filters
from frappe_app.models.core.user_type import UserType

class UserTypeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserType
        fields = ['id']

