import django_filters as filters
from frappe_app.models.desk.system_console import SystemConsole

class SystemConsoleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SystemConsole
        fields = ['id']

