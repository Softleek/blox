import django_filters as filters
from frappe_app.models.desk.console_log import ConsoleLog

class ConsoleLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ConsoleLog
        fields = ['id']

