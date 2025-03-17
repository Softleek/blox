import django_filters as filters
from frappe_app.models.core.activity_log import ActivityLog

class ActivityLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ActivityLog
        fields = ['id']

