import django_filters as filters
from frappe_app.models.frappe_core.module_profile import ModuleProfile

class ModuleProfileFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ModuleProfile
        fields = ['id']

