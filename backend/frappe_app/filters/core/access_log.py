import django_filters as filters
from frappe_app.models.core.access_log import AccessLog

class AccessLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AccessLog
        fields = ['id']

