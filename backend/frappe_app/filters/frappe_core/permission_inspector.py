import django_filters as filters
from frappe_app.models.frappe_core.permission_inspector import PermissionInspector

class PermissionInspectorFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PermissionInspector
        fields = ['id']

