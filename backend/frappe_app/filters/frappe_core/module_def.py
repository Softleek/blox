import django_filters as filters
from frappe_app.models.frappe_core.module_def import ModuleDef

class ModuleDefFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ModuleDef
        fields = ['id']

