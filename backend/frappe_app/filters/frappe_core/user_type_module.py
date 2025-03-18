import django_filters as filters
from frappe_app.models.frappe_core.user_type_module import UserTypeModule

class UserTypeModuleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserTypeModule
        fields = ['id']

