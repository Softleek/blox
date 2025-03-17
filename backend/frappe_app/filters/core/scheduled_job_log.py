import django_filters as filters
from frappe_app.models.core.scheduled_job_log import ScheduledJobLog

class ScheduledJobLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ScheduledJobLog
        fields = ['id']

