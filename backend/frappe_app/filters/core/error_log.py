import django_filters as filters
from frappe_app.models.core.error_log import ErrorLog

class ErrorLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ErrorLog
        fields = ['id']

