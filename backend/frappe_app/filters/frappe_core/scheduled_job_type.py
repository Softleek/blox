import django_filters as filters
from frappe_app.models.frappe_core.scheduled_job_type import ScheduledJobType

class ScheduledJobTypeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ScheduledJobType
        fields = ['id']

