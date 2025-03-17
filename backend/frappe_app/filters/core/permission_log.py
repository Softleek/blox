import django_filters as filters
from frappe_app.models.core.permission_log import PermissionLog

class PermissionLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PermissionLog
        fields = ['id']

