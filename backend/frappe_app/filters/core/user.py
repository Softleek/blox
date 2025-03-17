import django_filters as filters
from frappe_app.models.core.user import User

class UserFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = User
        fields = ['id']

